c.NotebookApp.tornado_settings = {
    'headers': {
        'Content-Security-Policy': "frame-ancestors http://df1c000c73f9.ngrok.io http://1c5e027b2f50.ngrok.io 'self'"
    },
#    'xsrf_cookie_kwargs': {'SameSite': "None", 'Secure': True},
    'cookie_options': {'samesite': "None", 'secure': True}
}
c.NotebookApp.disable_check_xsrfBool = True
#c.NotebookApp.tornado_settings = {"cookie_options": {"SameSite": "None", "Secure": True}}
c.NotebookApp.disable_check_xsrf = True

#c.NotebookApp.tornado_settings = {
#    'headers': {
#        'Content-Security-Policy': 'default-src https: ‘unsafe-inline’; connect-src https: wss: ; frame-ancestors self http://584241c843db.ngrok.io http://6d933ce44314.ngrok.io http://f3f1824b42f4.ngrok.io',
#    }
#}

# Set options for certfile, ip, password, and toggle off
# browser auto-opening
#c.NotebookApp.certfile = u'/home/jovyan/naihil.pem'
#c.NotebookApp.keyfile = u'/home/jovyan/naihil.key'
# Set ip to '*' to bind on all interfaces (ips) for the public server
#c.NotebookApp.ip = '*'
#c.NotebookApp.password = u'sha1:ca75ddb4f176:4807e67714096da3f0ea9c7fde01ff2ec778bae0'
#c.NotebookApp.open_browser = False

# It is a good idea to set a known, fixed port for server access
#c.NotebookApp.port = 9999
