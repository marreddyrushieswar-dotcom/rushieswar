import subprocess
import sys

def generate_cert():
    try:
        subprocess.run([
            "openssl", "req", "-x509", "-newkey", "rsa:2048",
            "-keyout", "server.key",
            "-out", "server.crt",
            "-days", "365",
            "-nodes",
            "-subj", "/CN=localhost"
        ], check=True)
        print("Certificate generated successfully")
    except Exception:
        print("OpenSSL not found. Install OpenSSL or use Git Bash.")
        sys.exit(1)

generate_cert()
