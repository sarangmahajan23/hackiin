const { app, BrowserWindow, ipcMain } = require('electron/main')
const path = require('node:path')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  })

  win.loadFile('index.html')
  var py = require('child_process').spawn('python', ['./attendance.py']);
            py.on('close', function() {
            event.sender.send('asynchronous-reply', '');
                });
}

app.whenReady().then(() => {
  createWindow()

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
  
})



app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
  var py = require('child_process').spawn('python', ['./attendance.py']);
  py.on('close', function() {
  event.sender.send('asynchronous-reply', '');
      });
})