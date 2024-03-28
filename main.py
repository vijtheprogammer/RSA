import random
import math

#checks if number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1): 
        if num % i == 0: #not prime either
            return False

    return True 

#generate prime number
def gen_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime): #generate until its prime
        prime = random.randint(min, max)
    
    return prime

def mod_inv(e, phi):
    for d in range(3, phi): 
        if (d * e) % phi == 1: 
            return d 
    raise ValueError("mod_inv does not exist")

p, q = gen_prime(1000, 5000), gen_prime(1000, 5000) #define p and q

#in case they're the same
while p == q:
    q = gen_prime(1000, 5000)

n = p * q

phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n - 1)

while math.gcd(e, phi_n) != 1: #as long as they're not coprime
    e = random.randint(3, phi_n - 1)

#to get private key
d = mod_inv(e, phi_n)

print("Public Key: ", e)
print("Private Key: ", d)
print("n: ", n)
print("phi_n: ", phi_n)
print("p: ", p)
print("q: ", q)

message = "Hello World"

#represented using ASCII characters
message_encoded = [ord(ch) for ch in message]

# (m ^ e) mod n = c
ciphertext = [pow(ch, e, n) for ch in message_encoded]

#pow(c, e, n) is equivalent to (c ^ e) mod n

print("Ciphertext: ", ciphertext)

#turns numbers back into ASCII numbers
message_encoded = [pow(ch, d, n) for ch in ciphertext]

#chr() function is opposite of ord() function
message = "".join(chr(ch) for ch in message_encoded)

print("Plaintext: ", message)