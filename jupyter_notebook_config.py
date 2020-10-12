c.JupyterHub.tornado_settings = {                                                            
  'headers': {                                                                               
    'Content-Security-Policy': "frame-ancestors 'self' http://localhost"                     
  }                                                                                          
}                                                                                            
c.NotebookApp.tornado_settings = {                                                           
  'headers': {                                                                               
    'Content-Security-Policy': "frame-ancestors 'self' http://localhost"                     
  }                                                                                          
}   
