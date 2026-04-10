# Secure File Transfer System using TLS and SHA-256

## Description
This project implements a secure file transfer system using Python. It uses TLS (SSL) encryption to ensure secure communication between client and server. The system supports resuming interrupted file transfers and verifies file integrity using SHA-256 hashing.

## Objectives
- Enable secure file transfer over a network
- Encrypt communication using TLS
- Support resuming interrupted file transfers
- Ensure file integrity using SHA-256 hashing

## Features
- Secure communication using SSL/TLS
- File transfer with resume support
- Handles partial file transfers
- SHA-256 hash verification
- Multi-client support using threading

## Technologies Used
- Python
- Socket Programming
- SSL/TLS (OpenSSL)
- SHA-256 Hashing

## Working
1. The server generates an SSL certificate using OpenSSL
2. A TLS connection is established between client and server
3. The client sends the file name
4. The server checks for existing partial files
5. File transfer resumes from the last received byte
6. After completion, a SHA-256 hash is generated for verification

## Project Structure
```
├── server.py
├── generate_cert.py
├── server.crt
├── server.key
├── storage/
└── README.md
```

## How to Run

### Step 1: Install OpenSSL
Ensure OpenSSL is installed on your system.

### Step 2: Generate Certificate
python generate_cert.py

### Step 3: Run Server
python server.py

### Step 4: Connect Client
Use a compatible client to send files securely.

## Output
Example:
[+] Connected from ('127.0.0.1', 12345)
[✓] Received file.txt

## Results
- Secure file transfer established using TLS
- File transfer resumes after interruption
- File integrity verified using SHA-256

