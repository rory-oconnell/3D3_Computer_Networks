from Crypto.PublicKey import RSA            # RSA will be used to encrypt the AES session key
from Crypto.Cipher import AES, PKCS1_OAEP   # AES will be used to encrypt the message
from Crypto.Random import get_random_bytes  # Random bytes will be used to generate the AES session key


data = "This is the encrypted message that will be sent to the server".encode("utf-8")
file_out = open("encrypted_data.bin", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read())
session_key = get_random_bytes(16)

def RSAEncrypt(data, recipient_key):
    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()

RSAEncrypt(data, recipient_key)