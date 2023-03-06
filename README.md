
# MERCURY README

## Very Important - The Following Libraries are required in order for this program to work
### - pip install pycrypto
### - pip install rsa
### - pip install pycryptodome
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Steps are listed below:

- Open the requisite files. These should include:
    - MERCURY_Server.py
    - MERCURY_Client.py
    - generateRSA.py
    - encryptAll.py
    - decryptAll.py

- Open a terminal window and navigate to the folder containing the files.

```
    C:\Users\roryo>cd OneDrive/Desktop/Computer Networks
```

- In VSCode, run the generateRSA.py file. This will create two files called private.pem and public.pem. These are the private and public keys for the RSA encryption.

- In VSCode, run the MERCURY_Server.py file. VSCode should indicate “MERCURY SERVER IS ONLINE AND READY TO RECEIVE”

- In the terminal window, run the MERCURY_Client.py file using the command: python MERCURY_Client.py

- Input your message to be sent to the server. Note that if you input a message that is over 1000 characters in length, message will be rejected and the user will be reprompted to enter a message. This is a security feature to prevent bad actors from flooding the server storage with a single message.

- You will also be prompted to enter a key. The key is an integer known only to sender and receiver. This is key is for the proprietary cipher method. The assumption is that this key is known to both parties. Note that any attempts to enter a non integer are rejected and reprompted.

- Press enter, you should get a message in the terminal window indicating that your message has been encrypted, received, and stored successfully.

```
    C:\Users\roryo\OneDrive\Desktop\Computer Networks>python MERCURY_Client.py
    Input message to be encrypted and sent to the server:Hello there, this is a test message for the ReadMe file.
    From Server: Your message has been encrypted, received, and stored successfully.
```

- The file has been encrypted using RSA and AES methodologies and has been sent to the server via a TCP connection, ensuring reliable, in order, and uncorrupted, transmission. In VSCode you can see that the encrypted message has been printed out for demonstration purposes.

- At this point in the overall idea, the encrypted message is converyed to an area with an internet connection via drone. The drone uploads the encrypted file to a cloud server, where it is then sent to the intended recipient. The next step is taken by the receiver to decode the message.

- Kill the running processes as the server is still listening for a message. 

- Navigate the decryptAll.py file, and run the program. This program will decrypt the AES Session key that was encrypted using RSA encryption. The decrypted AES key is then used to decrypt the message into the cipher. You will be prompted to enter the key for the cipher. Once entered, the cipher is translated back to the original message. Upon running the file, you will see the decrypted message print out in the VSCode terminal. The message has been transmitted securely.