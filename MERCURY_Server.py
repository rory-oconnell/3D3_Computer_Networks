from socket import* # Import socket module

messageStorage = [] # Create a list to store the messages

# Create a TCP socket
serverPort = 12000  # Reserve a port for your service.
serverSocket = socket(AF_INET, SOCK_STREAM) # Create a socket object
serverSocket.bind(('', serverPort)) # Bind to the port
serverSocket.listen(1)  # Now wait for client connection.
print ('MERCURY SERVER IS ONLINE AND READY TO RECEIVE') # Print a message when the server is ready to receive requests
while True:
    connectionSocket, addr = serverSocket.accept()  # Establish the connection
    sentence = connectionSocket.recv(1024)  # Receive the client packet
    messageStorage.append(sentence) # Append the message to the list

    MessageReceived = "Your message has been encrypted, received, and stored successfully." # Create a message to send back to the client to signify that the message has been received
    connectionSocket.send(MessageReceived.encode()) # Send the message back to the client
    print(messageStorage[0])    # Print the encrypted message to the server for demonstration purposes
    connectionSocket.close()    # Close the connection