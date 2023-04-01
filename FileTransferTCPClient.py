#!/usr/bin/env python3
from Crypto.Cipher import AES
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "1somehing.11somehing."  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print 'file opened'

    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

    # Encrypt file with AES   
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(f)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')


