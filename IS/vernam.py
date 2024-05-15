plain = input("Enter plain text: ")
print("Length of plain text is", len(plain))

key = input("Enter key value (length same as plain text): ")
print("Length of key is", len(key))

cipher = ""
decipher = ""

if len(key) != len(plain):
    print("Error! Length of key is not same as plain text!")
else:
    for i in range(0, len(plain)):
        encrypt = ord(plain[i]) ^ ord(key[i])
        cipher += chr(encrypt)

    print("Ciphered text:", cipher)

    for i in range(0, len(plain)):
        decrypt = ord(cipher[i]) ^ ord(key[i])
        decipher += chr(decrypt)

    print("Deciphered text:", decipher)
    
    
###############################################################
pt = 'hriday'
key = 'friday'

if len(key) != len(pt):
    print('errer')
else:
    ct = ''
    dt = ''
    for i in range(len(pt)):
        val = ord(pt[i]) ^ ord(key[i])
        ct += chr(val)
        
    print("Ciphered text:", ct)

    for j in range(len(key)):
        val = ord(ct[j]) ^ ord(key[j])
        dt += chr(val)
        
    print("Ciphered text:", dt)