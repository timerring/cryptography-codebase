import secrets
from random import randrange
import random


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


def KE_create(min_num: int, max_num: int) -> int:
    while 1:
        prime_ran: int = random.randint(min_num, max_num)
        if prime_ran % 2 == 0:
            prime_ran += 1
        if is_probably_prime_miller_rabin(prime_ran):
            break
    return prime_ran


# Extended Euclidean Algorithm
def ex_gcd(a, b) -> tuple:
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ex_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


# 定义快速模幂函数
def quick_mod(in_a: int, k: int, in_n: int) -> int:
    ans = 1
    while k != 0:
        if k % 2:
            ans = (ans % in_n) * (in_a % in_n) % in_n
        in_a = (in_a % in_n) * (in_a % in_n) % in_n
        k = k // 2
    return ans


# 定义求原根算法
def root(in_n: int) -> int:
    k = (in_n - 1) // 2
    # 查找512位左右的原根:
    for i in range(pow(2, 511), in_n - 1):
        if quick_mod(i, k, in_n) != 1:
            return i


# Read a decimal string representing a plaintext message . Raise an exception if is invalid.
plaintext: str = input('input the plaintext:\n')
# Generate a private key and the corresponding public key.
p_elgamal: int = get_big_prime()
# Print the private key and the public key as multiple decimal strings
print('\nPrivate Key:\n', 'p:\n', p_elgamal)
# 求p的原根alpha
alpha: int = root(p_elgamal)
print('alpha:\n', alpha)
# 选取一个a，a属于(2,p-2):
a: int = random.randint(2, p_elgamal - 2)
print('a:\n', a)
print('Public Key:\n', 'p:\n', p_elgamal)
print('alpha:\n', alpha)
beta: int = quick_mod(alpha, a, p_elgamal)
print('beta:\n', beta)

# 求满足条件的KE
KE = KE_create(pow(2, 511), p_elgamal - 2)
KE_inv: int = ex_gcd(KE, p_elgamal - 1)[0]

# Sign the message m . Print the signature as multiple decimal string (r,s).
r: int = pow(alpha, KE, p_elgamal)
s: int = (int(plaintext) - a * r) * KE_inv % (p_elgamal - 1)
print('\nSignature:\nr:\n', r)
print('\ns:\n', s)
# Verify the signature of message m. Print valid if the signature is valid. Print invalid otherwise.
t = (quick_mod(beta, r, p_elgamal) * quick_mod(r, s, p_elgamal)) % p_elgamal
print("Verify (r,s) of m:")
if t == quick_mod(alpha, int(plaintext), p_elgamal):
    print("valid")
else:
    print("invalid")

# Randomly pick a number as a faked message
plaintext_rnd: int = random.randint(pow(2, 511), pow(2, 512))
# verify the signature of message .
s_1: int = (int(plaintext) - a * r) * KE_inv % (p_elgamal - 1)
t_1 = quick_mod(beta, r, p_elgamal) * quick_mod(r, s_1, p_elgamal)
print("m' (faked):\n", plaintext_rnd)
# Print valid if the signature is valid. Print invalid otherwise
print("Verify s of m':")
if t_1 == quick_mod(alpha, int(plaintext), p_elgamal):
    print("valid")
else:
    print("invalid")

# Randomly pick numbers as a faked signature , and verify the signature of message .
r_rnd: int = random.randint(pow(2, 511), pow(2, 512))
s_rnd: int = (int(plaintext) - a * r_rnd) * KE_inv % (p_elgamal - 1)
print("r' (faked):\n", r_rnd)
print("s' (faked):\n", s_rnd)
t_2 = quick_mod(beta, r_rnd, p_elgamal) * quick_mod(r_rnd, s_rnd, p_elgamal)
print("Verify s' of m:")
# Print valid if the signature is valid. Print invalid otherwise.
if t_2 == quick_mod(alpha, int(plaintext), p_elgamal):
    print("valid")
else:
    print("invalid")
