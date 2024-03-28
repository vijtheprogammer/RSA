# RSA
Python RSA Implementation

RSA (Rivest-Shamir-Adleman) is a public-key cryptographic algorithm widely used for secure data transmission and encryption. It relies on the computational difficulty of factoring large prime numbers, making it highly secure when implemented correctly.

Here's a simplified explanation of the math behind RSA:

Key Generation:

Choose two distinct prime numbers, p and q.
Calculate their product, n = p * q. This is the modulus.
Calculate φ(n) = (p - 1)(q - 1), where φ is Euler's totient function.
Choose an integer e such that 1 < e < φ(n) and e is coprime with φ(n) (i.e., gcd(e, φ(n)) = 1). e is the public exponent.
Compute d as the modular multiplicative inverse of e modulo φ(n). In other words, d * e ≡ 1 (mod φ(n)). d is the private exponent.
Encryption:

To encrypt a message M, represented as an integer, compute C ≡ M^e (mod n). C is the ciphertext.
Decryption:

To decrypt the ciphertext C, compute M ≡ C^d (mod n). M is the original message.
Now, let's delve a bit into the mathematics involved:

Modular Exponentiation: Both encryption and decryption rely on modular exponentiation. In encryption, M^e (mod n) is calculated, and in decryption, C^d (mod n) is calculated. Modular exponentiation is efficient to compute even for very large numbers.

Key Security: The security of RSA relies on the difficulty of factoring the modulus n into its prime factors, p and q. Given a sufficiently large n (typically hundreds of digits long), it is computationally infeasible to factorize n into its prime factors using classical computers.

Public and Private Keys: The public key consists of (e, n) and is used for encryption. The private key consists of (d, n) and is used for decryption. The security of RSA depends on keeping the private key secret and making the public key widely available.

Decryption Using Private Key: Decryption works because of the mathematical relationship between e and d:

C^d ≡ (M^e)^d ≡ M^(e * d) ≡ M^1 (mod n) ≡ M (mod n).
This relies on Euler's theorem and the fact that d and e are multiplicative inverses modulo φ(n).
In summary, RSA encryption and decryption are based on modular exponentiation and the mathematical properties of prime numbers. Its security relies on the difficulty of factoring large composite numbers into their prime factors.
