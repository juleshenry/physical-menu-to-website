const { contextBridge, ipcRenderer } = require('electron');

// Expose protected methods that allow the renderer process to use
// the ipcRenderer without exposing the entire object
contextBridge.exposeInMainWorld('electronAPI', {
  processImages: (imagePaths) => ipcRenderer.invoke('process-images', imagePaths),
  extractColors: (imagePaths) => ipcRenderer.invoke('extract-colors', imagePaths)
});
