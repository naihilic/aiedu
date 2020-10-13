c.JupyterHub.tornado_settings = {                                                            
  'headers': {                                                                               
    'Content-Security-Policy': "frame-ancestors 'self' http://d4d5db0aad48.ngrok.io"                     
  }                                                                                          
}                                                                                            
c.NotebookApp.tornado_settings = {                                                           
  'headers': {                                                                               
    'Content-Security-Policy': "frame-ancestors 'self' http://d4d5db0aad48.ngrok.io"                     
  }                                                                                          
}   
c.Spawner.args = ["--NotebookApp.tornado_settings={                                          
  'headers':{                                                                                
    'Content-Security-Policy': \"frame-ancestors 'self' http://d4d5db0aad48.ngrok.io\",      
  }                                                                                          
}"] 
