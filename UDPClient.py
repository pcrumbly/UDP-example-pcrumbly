import socket

def main():
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific IP address and port
    server_address = ('localhost', 12345)

    # Send a message to the server
    while True:
        # Prompt the user to enter a message
        message = input('Enter a message to send: ')

        # Encode the message as bytes and send it to the server
        udp_socket.sendto(message.encode(), server_address)

        # Receive a message from the server
        data, _ = udp_socket.recvfrom(4096)

if __name__ == "__main__":
    main()
