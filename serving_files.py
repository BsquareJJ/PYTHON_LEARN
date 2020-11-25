import http.server
import socket

PORT = 8080

handler = http.server.SimpleHTTPRequestHandler
httpd = socket.TCPserver(("", PORT), handler)

print("[INFO]: SERVING FILES AT PORT {}".format(PORT))
httpd.serve_forever()