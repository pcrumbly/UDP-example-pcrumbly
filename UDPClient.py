import socket

def main():
    """
    Creates a UDP socket and binds it to a specific IP address and port.
    Continuously prompts the user to enter a message, encodes it as bytes,
    and sends it to a server using the socket. Then, receives a message
    from the server and prints it.

    Parameters:
        None

    Returns:
        None
    """
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
        print(f'Received message: {data.decode()}')

if __name__ == "__main__":
    main()
