from socket import*
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# Encryption function using RSA and AES
def AES_RSA_Encrypt(data, recipient_key):

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(sentence)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

def SecondEncrypt(message):

    key = input('What is the numeric key?')

    while key.isdigit() == False:
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
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input message to be encrypted and sent to the server:')

# Reprompt user if message is too long - security measure to stop single messages from flooding the server
while len(sentence) > 1000:
    print("Message is too long. Please try again.")
    sentence = input('Input message to be encrypted and sent to the server:')

sentence = SecondEncrypt(sentence)

sentence = sentence.encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)

AES_RSA_Encrypt(sentence, recipient_key)

payload = open("encrypted_data.bin", "rb").read()
clientSocket.send(payload)
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()

########################################################################################




