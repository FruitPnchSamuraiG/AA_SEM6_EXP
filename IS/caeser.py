mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i

print(mapping)

def ceasar_cipher(text,shift):
    ciphered_text = ''
    for char in text :
        char = char.upper()
        ciphered_value = (mapping[char] + shift ) % 26 
        ciphered_text += chr(65 + ciphered_value)            
    return ciphered_text

def ceasar_decipher(text,shift):
    deciphered_text = ''
    for char in text :
        char = char.upper()
        deciphered_value = (mapping[char] - shift ) % 26 
        deciphered_text += chr(65 + deciphered_value)
            
    return deciphered_text

plain_text = 'ABC'
plain_text = plain_text.replace(' ','')
print('Plain text : ',plain_text)

ciphered_text = ceasar_cipher(plain_text, -21)
print('Ciphered text:',ciphered_text)

deciphered_text = ceasar_decipher(ciphered_text, -21)
print('Deciphered text: ',deciphered_text)

###########################

mapping = {}

for i in range(26):
    mapping[chr(i+65)] = i

print(mapping)

def caesar(text, shift):
    ct = ''
    for char in text:
        char = char.upper()
        ct_value = (mapping[char] + shift) % 26
        ct += chr(ct_value+65)
    return ct

def dt_caesar(text, shift):
    ct = ''
    for char in text:
        char = char.upper()
        ct_value = (mapping[char] - shift) % 26
        ct += chr(ct_value+65)
    return ct

message = 'hriday'
ct = caesar(message, -21)
print(ct)
dt = dt_caesar(ct, -21)

print(dt)
