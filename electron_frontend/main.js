const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let pythonProcess = null;
const BACKEND_PORT = 8000;
const BACKEND_HOST = '127.0.0.1';

function startPythonBackend() {
  // In development, use the python command. 
  // In production, point to the bundled executable.
  const pythonPath = app.isPackaged 
    ? path.join(process.resourcesPath, 'backend/dist/main') 
    : 'python3';

  const backendScript = app.isPackaged
    ? [] // In production, executable doesn't need script path
    : [path.join(__dirname, '../python_backend/fastapi_server.py'), '--port', String(BACKEND_PORT)];

  console.log(`Starting Python backend: ${pythonPath} ${backendScript.join(' ')}`);
  
  pythonProcess = spawn(pythonPath, backendScript);
  
  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python Backend: ${data}`);
  });
  
  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python Backend Error: ${data}`);
  });
  
  pythonProcess.on('close', (code) => {
    console.log(`Python backend process exited with code ${code}`);
    pythonProcess = null;
  });
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile('pages/welcome.html');

  // Open DevTools in development
  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools();
  }

  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

app.whenReady().then(() => {
  startPythonBackend();
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

// Clean up the Python process on exit
app.on('will-quit', () => {
  if (pythonProcess) {
    console.log('Stopping Python backend...');
    pythonProcess.kill();
    pythonProcess = null;
  }
});

// IPC handlers for backend communication via FastAPI
ipcMain.handle('process-images', async (event, imagePaths) => {
  try {
    const response = await fetch(`http://${BACKEND_HOST}:${BACKEND_PORT}/process-images`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ image_paths: imagePaths }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.data || data;
  } catch (error) {
    console.error('Error processing images:', error);
    throw error;
  }
});

ipcMain.handle('extract-colors', async (event, imagePaths) => {
  try {
    const response = await fetch(`http://${BACKEND_HOST}:${BACKEND_PORT}/extract-colors`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ image_paths: imagePaths }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.colors || data;
  } catch (error) {
    console.error('Error extracting colors:', error);
    throw error;
  }
});
