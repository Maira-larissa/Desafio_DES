import random

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def generate_large_prime(bits=16):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p): return p

def find_generator(p):
    for g in range(2, p):
        if pow(g, (p-1)//2, p) != 1: return g
    return None

def diffie_hellman():
    p = generate_large_prime()
    g = find_generator(p)
    private = random.randint(1, p-1)
    public = pow(g, private, p)
    return private, public, p, g

def compute_shared_key(private, received_public, p):
    return pow(received_public, private, p)