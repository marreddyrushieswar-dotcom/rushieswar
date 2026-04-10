import socket
import ssl
import os
import hashlib

SERVER_IP = "172.20.10.2"   # CHANGE if server is remote
PORT = 5000
CHUNK_SIZE = 4096

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            h.update(chunk)
    return h.hexdigest()

filename = input("Enter file to upload: ")

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

with socket.create_connection((SERVER_IP, PORT), timeout=10) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_IP) as ssock:

        ssock.sendall(os.path.basename(filename).encode())

        offset = int(ssock.recv(1024).decode())

        with open(filename, "rb") as f:
            f.seek(offset)
            while chunk := f.read(CHUNK_SIZE):
                ssock.sendall(chunk)

        ssock.sendall(b"EOF")

        server_hash = ssock.recv(1024).decode()
        local_hash = sha256_file(filename)

        if server_hash == local_hash:
            print("Upload successful and verified")
        else:
            print("Integrity check failed")
