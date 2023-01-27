### Program : ElGamal (on group)

In this part, you are required to implement the ElGamal algorithm from scratch. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Return the private key $(p,\alpha,a)$ and the corresponding public key $(p,\alpha,\beta)$. The prime number $p$ should be approximately 512 bits. Note that finding a primitive root $\alpha$ in $\mathbb{F}_p$ might be time-consuming.
- Encrypt
  - Given a plaintext message $m \in \mathbb{F}_p$ and a public key $(p,\alpha,\beta)$, return the encrypted message $(r,t)$ and the secret key $k$.
- Decrypt
  - Given a ciphertext message $(r,t)$ and a private key $(p,\alpha,a)$, return the decrypted message $m^\prime$.

Your program does the following:

- Generate a private key and the corresponding public key. You may use the **Miller-Rabin Test** algorithm to determine whether an integer is prime. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Encrypt the message $m$. Print the encrypted message $(r,t)$ as multiple decimal strings.
- Decrypt the encrypted message $(r,t)$. Print the decrypted message $m^\prime$ as a decimal string.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- finding a primitive root modulo prime p

Note: you are not allowed to use **Extended Euclidean Algorithm** in this program.

#### Example Input & Output

Input:

```
4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
```

Output:

```txt
Private Key:
p: 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
alpha: 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729
a: 3101984266868748920462287182124446696068493916489350126886947863612185839382696504960710290519388739925364867918988436503372297381505951416202859274461749
Public Key:
p: 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
alpha: 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729
beta: 1159968293290431483618624548862401630355209517151486248093696597103338439113317368321706438200804727461211332263913961450514008706205896803328741922554539
Ciphertext:
r: 4270390275647605104323112550114089020700231211424317817144932009272298324070546918004125267551309710095448806447104314957099856583975262276729327418983805
t: 3221108136460372613636905604674169025183939828688657275543956232356097903511339858673306464341986911484482234789310340929730245929110146334280736926494309
Plaintext:
m': 4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
```

#### solution code
```python
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
```



[Return Home](https://github.com/timerring/cryptography-codebase)
