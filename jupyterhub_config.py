#c.Spawner.args = ["--NotebookApp.tornado_settings={ 'headers': { 'Content-Security-Policy': 'frame-ancestors http://46d2446d1b0b.ngrok.io \'self\''} }"]  
c.JupyterHub.tornado_settings = { 
  'headers': { 
    'Content-Security-Policy': "frame-ancestors http://df1c000c73f9.ngrok.io http://1c5e027b2f50.ngrok.io 'self'"
  },
#  'xsrf_cookie_kwargs': {'SameSite': "None", 'Secure': True},
  'cookie_options': {'samesite': "None", 'secure': True}
}
c.JupyterHub.disable_check_xsrfBool = True
#c.JupyterHub.disable_check_xsrf = True
#c.Spawner.args = [ '--config=/home/jovyan/jupyter_notebook_config.py']
#c.JupyterHub.tornado_settings = {"cookie_options": {"SameSite": "None", "Secure": True}}
