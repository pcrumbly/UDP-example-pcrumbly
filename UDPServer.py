import socket

def main():
    """
    Main function to create and bind a UDP socket,
    receive messages, and send a response back to the client.
    """
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific IP address and port
    server_address = ('localhost', 12345)
    sock.bind(server_address)

    while True:
        # Wait for a message to be received
        print('Waiting for a message...')
        data, address = sock.recvfrom(4096)
        print(f'Received message: {data.decode()}')

        # Send a response back to the client
        response = 'Message received'
        sock.sendto(response.encode(), address)

if __name__ == '__main__':
    main()
