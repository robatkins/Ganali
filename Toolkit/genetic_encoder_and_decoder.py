#GANALI
#DNA Encoder and Decoder


def string_to_bits(input_string):
    # Convert each character to its binary representation
    binary_list = [bin(ord(char))[2:].zfill(8) for char in input_string]

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

    # Map each DNA base pair to its binary representation and join them
    result_string = ''.join(base_pairs[dna_pair] for dna_pair in dna_pairs)

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
input_string = input("Enter a string: ")
bits_representation = string_to_bits(input_string)
print()

if query_encrypt_or_decrypt.lower() == 'encrypt':
    print("Bit Representation: " + bits_representation)
    print() 
    dna_encoded_bits = bits_to_dna_base_pair(bits_representation)
    print("Bit Encoded DNA Sequence: " + dna_encoded_bits)
    print()

if query_encrypt_or_decrypt.lower() == 'decrypt':
    dna_bits = dna_base_pair_to_bits(input_string)
    decoded_string = bits_to_string(dna_bits)
    print(decoded_string)
