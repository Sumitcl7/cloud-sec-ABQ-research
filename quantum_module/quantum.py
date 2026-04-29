import hashlib

def quantum_encrypt(data):
    # Simulating post-quantum encryption using hashing
    data_str = str(data)
    encrypted = hashlib.sha3_256(data_str.encode()).hexdigest()
    return encrypted