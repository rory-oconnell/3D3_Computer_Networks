
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
    - encryptRSA.py
    - decryptRSA.py

- Open a terminal window and navigate to the folder containing the files.

```
    C:\Users\roryo>cd OneDrive/Desktop/Computer Networks
```

- In VSCode, run the generateRSA.py file. This will create two files called private.pem and public.pem. These are the private and public keys for the RSA encryption.

- In VSCode, run the MERCURY_Server.py file. VSCode should indicate “MERCURY SERVER IS ONLINE AND READY TO RECEIVE”

- In the terminal window, run the MERCURY_Client.py file using the command: python MERCURY_Client.py

- Input your message to be sent to the server. Note that if you input a message that is over 1000 characters in length, message will be rejected and the user will be reprompted to enter a message. This is a security feature to prevent bad actors from flooding the server storage with a single message.

- Press enter, you should get a message in the terminal window indicating that your message has been encrypted, received, and stored successfully.

```
    C:\Users\roryo\OneDrive\Desktop\Computer Networks>python MERCURY_Client.py
    Input message to be encrypted and sent to the server:Hello there, this is a test message for the ReadMe file.
    From Server: Your message has been encrypted, received, and stored successfully.
```

- The file has been encrypted using RSA and AES methodologies and has been sent to the server via a TCP connection, ensuring reliable, in order transmission. In VSCode you can see that the encrypted message has been printed out for demonstration purposes.

- Navigate the decryptRSA.py file, and run the program. You may need to kill the running processes as the server is still listening for a message. Upon running the file, you will see the decrypted message print out in the VSCode terminal.
