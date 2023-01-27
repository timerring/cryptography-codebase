# Program 1: Textbook RSA (on group)
from random import randrange
import secrets
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


def get_big_prime(nbits: int) -> int:
    # http://ju.outofmemory.cn/entry/93761
    # 返回一个可能是素数的大整数
    while True:
        p: int = 2 ** (nbits - 1) | secrets.randbits(nbits)
        # Miller_Robin算法对2的倍数检测有异常，故如果生成2的倍数，则将其+1再进行判断:
        if p % 2 == 0:
            p = p + 1
        if is_probably_prime_miller_rabin(p):
            return p


def E_create(min_num: int, max_num: int) -> int:
    while 1:
        prime_ran: int = random.randint(min_num, max_num)
        if prime_ran % 2 == 0:
            prime_ran += 1
        if is_probably_prime_miller_rabin(prime_ran):
            break
    return prime_ran


# 定义扩展欧几里得算法:
def ex_gcd(a, b) -> tuple:
    if b == 0:
        return 1, 0, a
    else:
        x, y, q = ex_gcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y, q


# 生成p,q:
p: int = get_big_prime(512)
q: int = get_big_prime(512)
n: int = p * q
# 求n:
phi_n: int = (p - 1) * (q - 1)
print('Private key:\n', 'N:\n', n)
# 选择与n互素的e:
e: int = E_create(pow(2, 1023), n)

# 输出d(逆元):
d: int = ex_gcd(e, phi_n)[0]
print('d:\n', d)
print('Public key:\n', 'N:\n', n)
print('e:\n', e)
# Read a decimal string representing a plaintext message m.
# Raise an exception if m is invalid:
plaintext: str = input('input the plaintext:\n')
if int(plaintext) < 0:
    raise ValueError
# Sign the message m. Print the signature as a decimal string.:
s: int = pow(int(plaintext), d, n)
print('\nSignature:\ns:\n', s)
plaintext_ver: int = pow(s, e, n)
print("Verify s of m:")
# Verify the signature of message .
if plaintext_ver == int(plaintext):
    print("valid")
else:
    print("invalid")

# Randomly pick a number as a faked message
plaintext_rnd: int = random.randint(pow(2, 1023), pow(2, 1024))
# verify the signature of message .
s_1: int = pow(plaintext_rnd, d, n)
plaintext_ver_1: int = pow(s_1, e, n)
print("m' (faked):\n", plaintext_ver_1)
print("Verify s of m':")
if plaintext_ver_1 == int(plaintext):
    print("valid")
else:
    print("invalid")

# Randomly pick a number as a faked signature
s_2: int = random.randint(pow(2, 1023), pow(2, 1024))
# verify the signature of message .
plaintext_ver_2: int = pow(s_2, e, n)
print("s' (faked):\n", s_2)
print("Verify s' of m:")
if plaintext_ver_2 == int(plaintext):
    print("valid")
else:
    print("invalid")
