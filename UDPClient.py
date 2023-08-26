import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 12345)

while True:
    message = input('Enter a message to send: ')

    # Send the message to the server
    sock.sendto(message.encode(), server_address)

    # Wait for a response from the server
    data, _ = sock.recvfrom(4096)
    print(f'Response from server: {data.decode()}')
