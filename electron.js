const { app, BrowserWindow } = require('electron');
const path = require('path');
const url = require('url');

let mainWindow

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });

  mainWindow.loadURL(
    process.env.ELECTRON_START_URL || `file://${__dirname}/../build/index.html`
  )
  mainWindow.on('closed', () => {
    mainWindow = null
  })
  win.loadFile(path.join(__dirname, '../build/index.html'));
}

app.whenReady().then(createWindow);

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})