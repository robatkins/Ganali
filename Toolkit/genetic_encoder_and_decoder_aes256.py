#GANALI
#DNA Encoder and Decoder with AES-256

import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import base64
import binascii  # Import the binascii module

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_string(input_string, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)

    plaintext = input_string.encode('utf-8')

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return salt + iv + ciphertext

def decrypt_string(encrypted_data, password):
    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    ciphertext = encrypted_data[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_data.decode('utf-8')


def string_to_bits(input_bytes):
    # Convert each byte to its binary representation
    binary_list = [bin(byte)[2:].zfill(8) for byte in input_bytes]

    # Join the binary representations into a single string
    binary_string = ''.join(binary_list)

    return binary_string


def bits_to_string(bits):
    # Split the binary string into 8-bit substrings
    eight_bit_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]

    # Convert each 8-bit substring to its decimal representation and then to a character
    characters = [chr(int(chunk, 2)) for chunk in eight_bit_chunks]

    # Join the characters into a single string
    result_string = ''.join(characters)

    return result_string

def bits_to_dna_base_pair(bits):
    # Split the sequence of bits into individual bits
    bit_pairs = [bits[i:i+1] for i in range(0, len(bits), 1)]

    # Map each bit pair to its DNA base pair
    base_pairs = {'0': 'AT', '1': 'CG'}
    result_string = ''.join(base_pairs[bit_pair] for bit_pair in bit_pairs)

    return result_string

def dna_base_pair_to_bits(dna_sequence):
    # Map each DNA base pair to its binary representation
    base_pairs = {'AT': '0', 'CG': '1'}
    
    # Split the DNA sequence into base pairs
    dna_pairs = [dna_sequence[i:i+2] for i in range(0, len(dna_sequence), 2)]

    try:
        # Map each DNA base pair to its binary representation and join them
        result_string = ''.join(base_pairs[dna_pair] for dna_pair in dna_pairs)
    except KeyError as e:
        print(f"Error: Invalid DNA base pair encountered - {e}")
        result_string = ""

    return result_string

# Get input from the user
while True:
    query_encrypt_or_decrypt = input("Enter encrypt or decrypt: ")
    if query_encrypt_or_decrypt.lower() in ['encrypt', 'decrypt']:
        break
    else:
        print("Invalid input. Please enter either 'encrypt' or 'decrypt'.")

# Get input from the user
print()
password = input("Enter the password: ").strip()
print()
input_string = input("Enter a string: ")
print()

if query_encrypt_or_decrypt.lower() == 'encrypt':
    #Encrypt the User Input
    encrypted_data = encrypt_string(input_string, password)
    print("AES-256 Encrypted String: " + base64.b64encode(encrypted_data).decode('utf-8'))
    print()
    #Get the Bits Representation of the Encrypted String
    bits_representation = string_to_bits(encrypted_data)
    print("Bit Representation: " + bits_representation)
    print() 
    #Encode the bits as a DNA Sequence
    dna_encoded_bits = bits_to_dna_base_pair(bits_representation)
    print("Bit Encoded DNA Sequence: " + dna_encoded_bits)
    print()
