from socket import*

messageStorage = []

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('MERCURY SERVER IS ONLINE AND READY TO RECEIVE')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    messageStorage.append(sentence)

    MessageReceived = "Your message has been encrypted, received, and stored successfully."
    connectionSocket.send(MessageReceived.encode())
    print(messageStorage[0])
    connectionSocket.close()