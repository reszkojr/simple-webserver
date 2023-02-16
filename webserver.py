from socket import *

def create_server():
    server_socket = socket(AF_INET, SOCK_STREAM) # Instantiating a new socket
    try:
        server_socket.bind(('localhost', 8080)) # Binding a socket on host 'localhost' and port '8080'
        server_socket.listen(5)                 # Queue upcoming clients

        while True:
            (clientsocket, address) = server_socket.accept()    # Wait for an upcoming connection
            
            # read = clientsocket.recv(5000).decode()             # Read client's request (We're not using it)
            # pieces = read.split('\n')
            # if ( len(pieces) > 0 ) : print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body> Hello World</body></html>\r\n"
            data += "\r\n\r\n" # Telling the client that we're closing the connection

            clientsocket.sendall(data.encode()) # Sending the encoded data as UTF-8 to the client 
            clientsocket.shutdown(SHUT_RD)      # Closing the connection

    except Exception as exc:
        print('Error:')
        print(exc)

        print('\nShutting down...\n')

print('Try accessing http://localhost:8080')
create_server()
