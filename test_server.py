# Import socket module
from socket import *

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The web server is up on port:', serverPort)

while True:
    print('Ready to serve...')
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()

        if not message:
            break

        # Send an HTTP response with a Content-Type header
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'
        response += '<html><body><h1>Hello, World!</h1></body></html>'
        connectionSocket.send(response.encode())

        connectionSocket.close()

    except Exception as e:
        print(f"Error: {e}")
        connectionSocket.close()
