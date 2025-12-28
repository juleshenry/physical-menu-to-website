const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;

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
  createWindow();

  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit();
});

// IPC handlers for backend communication
ipcMain.handle('process-images', async (event, imagePaths) => {
  return new Promise((resolve, reject) => {
    // Path to Python backend
    const pythonBackend = path.join(__dirname, '../python_backend/smart_menu.py');
    
    // Spawn Python process
    const pythonProcess = spawn('python3', [pythonBackend, ...imagePaths]);
    
    let output = '';
    let error = '';
    
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
      error += data.toString();
    });
    
    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(error || 'Python process failed'));
      } else {
        try {
          resolve(JSON.parse(output));
        } catch (e) {
          resolve({ raw: output });
        }
      }
    });
  });
});

ipcMain.handle('extract-colors', async (event, imagePaths) => {
  return new Promise((resolve, reject) => {
    const pythonBackend = path.join(__dirname, '../python_backend/smart_color.py');
    
    const pythonProcess = spawn('python3', [pythonBackend, ...imagePaths]);
    
    let output = '';
    let error = '';
    
    pythonProcess.stdout.on('data', (data) => {
      output += data.toString();
    });
    
    pythonProcess.stderr.on('data', (data) => {
      error += data.toString();
    });
    
    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(error || 'Python process failed'));
      } else {
        try {
          resolve(JSON.parse(output));
        } catch (e) {
          resolve({ raw: output });
        }
      }
    });
  });
});
