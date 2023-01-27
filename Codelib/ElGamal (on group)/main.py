import random
import secrets
from random import randrange

def is_probably_prime_miller_rabin(n: int, k: int = 10) -> bool:
    # Miller-Rabin 素数判定
    # https://gist.github.com/bnlucas/5857478
    if n == 2 or n == 3:
        return True
    if not n & 1:
        return False

    def check(a: int, s: int, d: int, n: int) -> bool:
        x = pow(a, d, n)
        if x == 1:
            return True
        for _ in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s: int = 0
    d: int = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for _ in range(k):
        a: int = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False

    return True


def get_big_prime(nbits: int = 512) -> int:
    # http://ju.outofmemory.cn/entry/93761
    # 返回一个可能是素数的大整数
    while True:
        p: int = 2 ** (nbits - 1) | secrets.randbits(nbits)
        if p % 2 == 0:
            p = p + 1
        if is_probably_prime_miller_rabin(p):
            return p

def generate_prime_factors(n):
    i = 2
    prime_factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in prime_factors:
                prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors

# Note that finding a primitive root in might be time-consuming.
def find_primitive_root(p):
    order = p - 1
    if p == 2:
        return 1

    prime_factors = generate_prime_factors(order)

    while True:
        g = random.randint(2, order)

        flag = False
        for factor in prime_factors:
            # pow -> pow(base, exponent, modulo)
            if pow(g, order // factor, p) == 1:
                flag = True
                break
        if flag:
            continue
        return g

# Given a plaintext message and a public key , return the encrypted message and the secret key .
def encrypt(in_mess, km):
    cipher_text: int = int((in_mess * km)) // p

    return cipher_text


# 扩展欧几里得求逆元
# reference:https://blog.csdn.net/weixin_44932880/article/details/118385473
def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ext_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


def ModReverse(a, p):
    x, y, q = ext_gcd(a, p)
    if q != 1:
        raise Exception("No solution.")
    else:
        return (x + p) % p


# Given a ciphertext message and a private key , return the decrypted message .
def decrypt(in_t, in_ke, in_d, in_p):
    km = pow(in_ke, in_d, in_p)
    km_inverse = ModReverse(km, in_p)
    plaintext = in_t * km_inverse
    return plaintext


if __name__ == '__main__':
    # Read a decimal string representing a plaintext message . Raise an exception if is invalid.
    mess: str = input("message input:")
    # Raise an exception if m is invalid
    try:
        not mess.isdecimal()
    except ValueError:
        print('message is invalid')
    p = get_big_prime(512)
    alpha = find_primitive_root(p)
    d = random.randint(2, p - 2)
    beta = pow(alpha, d, p)
    a = random.randint(2, p - 2)
    ephemeral_key = pow(alpha, a, p)
    masking_key_1 = pow(beta, a, p)
    # Print the private key and the public key as multiple decimal strings.
    print('Private Key:\np:', p, '\nalpha:', alpha, '\na:', a)
    print('Public Key:\np:', p, '\nalpha:', alpha, '\nbeta:', beta)
    # Encrypt the message . Print the encrypted message as multiple decimal strings.
    r = ephemeral_key
    t = encrypt(mess, masking_key_1)
    print('Ciphertext:\nr:', r, '\nt:', t)
    #Decrypt the encrypted message . Print the decrypted message as a decimal string.
    m = decrypt(t, ephemeral_key, d, p)
    print('Plaintext:\nm:', m)