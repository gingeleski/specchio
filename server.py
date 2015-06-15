import SimpleHTTPServer
import SocketServer

PORT = 5000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(('', PORT), Handler)

print 'Serving at port', PORT
print 'Navigate to localhost:' + str(PORT) + ' in the browser'
httpd.serve_forever()
