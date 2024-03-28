Prime Number Generation:

The code defines a function is_prime(num) to check if a number is prime.
Another function gen_prime(min, max) generates a prime number within a given range by repeatedly generating random numbers until a prime one is found.
Key Generation:

Two prime numbers p and q are generated using the gen_prime() function.
The modulus n is calculated as the product of p and q.
Euler's totient function phi(n) is computed.
A public exponent e is randomly chosen such that it is coprime with phi(n) (gcd(e, phi(n)) = 1).
The private exponent d is calculated using the modular inverse of e modulo phi(n).
Encryption:

The message "Hello World" is encoded into a list of ASCII values.
Each ASCII value is encrypted using the public key (e, n) and the ciphertext is computed using modular exponentiation.
Decryption:

The ciphertext is decrypted using the private key (d, n) and modular exponentiation.
The decrypted ASCII values are converted back to characters using the chr() function and joined together to form the plaintext message.
Output:

The program prints out the public key, private key, modulus n, Euler's totient phi(n), prime numbers p and q, ciphertext, and the decrypted plaintext message.
