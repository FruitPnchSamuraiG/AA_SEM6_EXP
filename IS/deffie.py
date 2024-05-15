# # Alice and Bob public keys = (P,G)
# P = 23
# G = 9

# # Alice and Bobs private keys selected
# pa = 4
# pb = 3

# def key_generator(P,G,p):
#     return (G**p) % P


# def secret_key_generator(P,gen_key,p):
#     return (gen_key**p) % P

# # exchange of generated keys takes place ( hard coded )
# gen_key_x = key_generator(P,G,pa)
# gen_key_y = key_generator(P,G,pb)

# # getting generated secret keys 
# ka = secret_key_generator(P,gen_key_y,pa)
# kb = secret_key_generator(P,gen_key_x,pb)
# print(ka)
# print(kb)

# if ka == kb:
#     print('Keys have been exchanged succesfully!')
    
#######################################################################
base = 5
mod = 23

pa = 4
pb = 3

def public_key_gen(base, mod, p):
    return pow(base, p) % mod


def secret_key(exchange_base, mod, p):
    return pow(exchange_base, p) % mod


Xa = public_key_gen(base, mod, pa)
Xb = public_key_gen(base, mod, pb)

#exchane

k1 = secret_key(Xb, mod, pa)
k2 = secret_key(Xa, mod, pb)

print(k1)
print(k2)

if k1 == k2:
    print('Keys have been exchanged succesfully!')
