# sender.py
import socket
from des import generate_private_key, compute_public_key, compute_shared_key, encrypt_message

class Sender:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.private_key = generate_private_key()
        self.public_key = compute_public_key(self.private_key)

    def send(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(str(self.public_key).encode('utf-8'))
            shared_key = compute_shared_key(int(s.recv(1024).decode('utf-8')), self.private_key)
            encrypted_message = encrypt_message(message, shared_key)
            s.sendall(encrypted_message.encode('utf-8'))
            print(f"Mensagem criptografada enviada: {encrypted_message}")

if __name__ == "__main__":
    sender = Sender()
    sender.send("Hello, Diffie-Hellman!")
