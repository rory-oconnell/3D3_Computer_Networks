from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

def SecondDecrypt(message):
    key = int(input('what is the numeric key?\n'))
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
private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
file_in.close()

# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)

data = SecondDecrypt(data.decode("utf-8"))

print(data)
