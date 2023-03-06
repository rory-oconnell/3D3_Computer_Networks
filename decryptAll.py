from Crypto.PublicKey import RSA    # RSA will be used to encrypt the AES session key
from Crypto.Cipher import AES, PKCS1_OAEP   # AES will be used to encrypt the message

def SecondDecrypt(message):
    key = input('Please enter the numeric key known only to you and the sender...\n')

    while key.isdigit() == False:   # Check if the key is an integer
        print("The key must be an integer. Please try again.")
        key = input('What is the numeric key?')

    key = int(key)
    temp2=''
    decrypt =[]
    for i in message:
        for j in i:
                if j != ' ':
                    num = ord(j) - key 
                    char = chr(num)
                    temp2 = temp2 + char 
                else:
                    temp2 = temp2 + ' '
    
    decrypt.append(temp2[::-1])  
    straight = ''.join((decrypt))
    return(straight)

file_in = open("encrypted_data.bin", "rb")
private_key = RSA.import_key(open("private.pem").read())    # Import the private key

enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]   # Read the encrypted data from the file
file_in.close() # Close the file

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)    # Create a cipher object using the private key
session_key = cipher_rsa.decrypt(enc_session_key)   # Decrypt the session key

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)  # Create a cipher object using the session key
data = cipher_aes.decrypt_and_verify(ciphertext, tag)   # Decrypt the message using the cipher object

data = SecondDecrypt(data.decode("utf-8"))  # Decode the message from bytes

print(data) # Print the message
