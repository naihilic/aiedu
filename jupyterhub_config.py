#c.Spawner.args = ["--NotebookApp.tornado_settings={ 'headers': { 'Content-Security-Policy': 'frame-ancestors http://46d2446d1b0b.ngrok.io \'self\''} }"]  
c.JupyterHub.tornado_settings = { 
  'headers': { 
    'Content-Security-Policy': "frame-ancestors http://46d2446d1b0b.ngrok.io 'self'"
  },
  'cookie_options': {'SameSite': "None", 'Secure': True}
}
c.JupyterHub.disable_check_xsrf = True
#c.Spawner.args = [ '--config=/home/jovyan/jupyter_notebook_config.py']
#c.JupyterHub.tornado_settings = {"cookie_options": {"SameSite": "None", "Secure": True}}
