import socket

# Our local host number
HOST = '127.0.0.1'

# You can use whatever port number
PORT = 4040

# Think of the AF_INET as an  IPV4 connection or a layer 3 protocol

channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
