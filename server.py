import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("192.168.122.45")
PORT = 8113

server_socket.bind((host, PORT))

while True:
	client_socket, address = server_socket.accept()
	print("Recieved connexion from {}".format(address))
	client_socket.send("Thank you for connecting to our network")
	client_socket.close()