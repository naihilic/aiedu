c.Spawner.args = ["--NotebookApp.tornado_settings={ 'headers': { 'Content-Security-Policy': 'frame-ancestors * self 'frame-ancestors self http://584241c843db.ngrok.io http://6d933ce44314.ngrok.io http://f3f1824b42f4.ngrok.io''} }"]  
c.JupyterHub.tornado_settings = { 
  'headers': { 
    'Content-Security-Policy': 'frame-ancestors self http://584241c843db.ngrok.io http://6d933ce44314.ngrok.io http://f3f1824b42f4.ngrok.io' 
  } 
} 
