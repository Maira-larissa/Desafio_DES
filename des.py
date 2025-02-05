# des.py
import random

# Parâmetros públicos para Diffie-Hellman
P = 23  # Número primo
G = 5   # Base

def generate_private_key():
    return random.randint(1, P-1)

def compute_public_key(private_key):
    return (G ** private_key) % P

def compute_shared_key(public_key, private_key):
    return (public_key ** private_key) % P

def encrypt_message(message, key):
    return ''.join(chr(ord(c) ^ key) for c in message)

def decrypt_message(encrypted_message, key):
    return ''.join(chr(ord(c) ^ key) for c in encrypted_message)
