# receiver.py
import socket
from des import generate_private_key, compute_public_key, compute_shared_key, decrypt_message

class Receiver:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.private_key = generate_private_key()
        self.public_key = compute_public_key(self.private_key)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print("Aguardando conexões...")
            conn, addr = s.accept()
            with conn:
                sender_public_key = int(conn.recv(1024).decode('utf-8'))
                conn.sendall(str(self.public_key).encode('utf-8'))
                shared_key = compute_shared_key(sender_public_key, self.private_key)
                encrypted_message = conn.recv(1024).decode('utf-8')
                decrypted_message = decrypt_message(encrypted_message, shared_key)
                print(f"Mensagem recebida e descriptografada: {decrypted_message}")

if __name__ == "__main__":
    receiver = Receiver()
    receiver.start()
