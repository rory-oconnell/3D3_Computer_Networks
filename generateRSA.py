from Crypto.PublicKey import RSA        # RSA will be used to encrypt the AES session key

key = RSA.generate(2048)    # Generate a private/public key pair using 2048 bits
private_key = key.export_key()  # Export the private key
file_out = open("private.pem", "wb")    # Open a file to write the private key to
file_out.write(private_key) # Write the private key to the file
file_out.close()    # Close the file

public_key = key.publickey().export_key()   # Export the public key
file_out = open("receiver.pem", "wb")   # Open a file to write the public key to
file_out.write(public_key)  # Write the public key to the file
file_out.close()    # Close the file