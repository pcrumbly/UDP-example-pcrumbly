# UDPClient and UDPServer
UDP client and server implementation in Python.

## UDPClient
  UDPClient: sends messages to a UDP server.

### Usage

1. Start the UDP server by running the `UDPServer.py` script.
2. Run the `UDPClient.py` script to start the UDP client.
3. Enter a message to send to the server when prompted.
4. The client will send the message to the server and display the response received.

## UDPServer

The UDPServer is a simple server program that receives messages from UDP clients.

### Usage

1. Run the `UDPServer.py` script to start the UDP server.
2. The server will listen for incoming messages from UDP clients.
3. When a message is received, the server will display the message and send a response back to the client.

## Dependencies
The UDPClient and UDPServer scripts require Python 3 and the `socket` module.
