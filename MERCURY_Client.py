from socket import*                     # Import socket module
from Crypto.PublicKey import RSA        # RSA will be used to encrypt the AES session key
from Crypto.Random import get_random_bytes  # Random bytes will be used to generate the AES session key
from Crypto.Cipher import AES, PKCS1_OAEP   # PKCS1_OAEP is the RSA encryption algorithm, AES is the AES encryption algorithm

# Encryption function using RSA and AES
def AES_RSA_Encrypt(data, recipient_key):

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)  # Create a cipher object using the public key
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX) # Create a cipher object using the session key
    ciphertext, tag = cipher_aes.encrypt_and_digest(sentence)   # Encrypt the message using the cipher object
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ] # Write the encrypted data to a file
    file_out.close()    # Close the file

def SecondEncrypt(message): # This function will encrypt the message using a Caesar cipher
    key = input('What is the numeric key known only to you and the receiver?') # Get the key from the user

    while key.isdigit() == False:   # Check if the key is an integer
        print("The key must be an integer. Please try again.")
        key = input('What is the numeric key?')

    key = int(key)

    words = message.split(' ')
    new_string = []
    temp= ''
    for i in words:
        for j in i:
        
            num = ord(j) + key
            char = chr(num)   
            temp = temp + char
        temp = temp + ' ' # see if we wanna keep this 
    new_string.append(temp[::-1]) 

    reverse = ''.join(reversed(new_string))
    return(reverse)

# Main
serverName = 'localhost'    # Server name
serverPort = 12000        # Server port
clientSocket = socket(AF_INET, SOCK_STREAM) # Create a socket object
clientSocket.connect((serverName, serverPort))  # Connect to the server
sentence = input('Input message to be encrypted and sent to the server:')

# Reprompt user if message is too long - security measure to stop single messages from flooding the server
while len(sentence) > 1000: # 1000 is an arbitrary number, but should limit messages to a reasonable size
    print("Message is too long. Please try again.")
    sentence = input('Input message to be encrypted and sent to the server:')

sentence = SecondEncrypt(sentence)  # Encrypt the message using the Caesar cipher

sentence = sentence.encode("utf-8") # Encode the message to bytes
file_out = open("encrypted_data.bin", "wb") # Open a file to write the encrypted data to

recipient_key = RSA.import_key(open("receiver.pem").read()) # Import the public key
session_key = get_random_bytes(16)  # Generate a random session key

AES_RSA_Encrypt(sentence, recipient_key)    # Encrypt the message using the AES and RSA algorithms

payload = open("encrypted_data.bin", "rb").read()   # Read the encrypted data from the file
clientSocket.send(payload)  # Send the encrypted data to the server
modifiedSentence = clientSocket.recv(1024)  # Receive the decrypted message from the server
print ('From Server:', modifiedSentence.decode())   # Print the decrypted message
clientSocket.close()    # Close the socket

########################################################################################




