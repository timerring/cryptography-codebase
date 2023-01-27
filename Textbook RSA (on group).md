### Program : Textbook RSA (on group)

In this part, you are required to implement the textbook RSA algorithm from scratch. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Return the private key $(N,d)$ and the corresponding public key $(N,e)$. The prime number $p$ and $q$ should be approximately 512 bits and therefore the RSA modulus number $N$ should be approximately 1024 bits. Note that finding an encryption exponent $e$ might be time-consuming.
- Encrypt
  - Given a plaintext message $m \in \mathbb{Z}_N$ and a public key $(N,e)$, return the encrypted message $c$.
- Decrypt
  - Given a ciphertext message $c \in \mathbb{Z}_N$ and a private key $(N,d)$, return the decrypted message $m^\prime$.

Your program does the following:

- Generate a textbook RSA key pair. You may use the **Miller-Rabin Test** algorithm to determine whether an integer is prime. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Encrypt the message $m$. Print the encrypted message $c$ as a decimal string.
- Decrypt the encrypted message $c$. Print the decrypted message $m^\prime$ as a decimal string.
- If you think the textbook RSA algorithm is secure, print `secure`. Print `insecure` otherwise.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- **Extended Euclidean Algorithm** 

Recall that including any third-party codes without claiming is considered as lack of academic integrity, and results in failing this course.

#### Example Input & Output

Input:

```txt
34862844108815430278935886114814204661242105806196134451262421197958661737288465541172280522822644267285105893266043422314800759306377373320298160258654603531159702663926160107285223145666239673833817786345065431976764139550904726039902450456522584204556470321705267433321819673919640632299889369457498214445
```

Output:

```txt
Private key:
N: 72480887416135972061737686062889407161759160887103574047817069443537714713215543172947835307344891172810092267953794611202591069661157992794959838750479208506005687981686025809332691431473809292764988868581099330149458758861391108410825625141738698507086062910615219209815042032904395035912581683751821198857
d: 32680572261276319950892386078453159129961789301515586779730994965995850002546722461272347997633819895532355760655076469284315213156424132333399966484423792583164625536594707257030835906698882316535262007407891728303620471604461013849133230965147690242465484589704113381685121927918786879123393719930911981301
Public key:
N: 72480887416135972061737686062889407161759160887103574047817069443537714713215543172947835307344891172810092267953794611202591069661157992794959838750479208506005687981686025809332691431473809292764988868581099330149458758861391108410825625141738698507086062910615219209815042032904395035912581683751821198857
e: 33917284234023552492304328018336609591997179645740843023623954792230653601864281593260663435095146463818240660159742130550887732511002455913550343095875105353898810744096024635824071115264943251609500722062745618030825015239681817073644641294390347390699708726562812289026328860966096616801710266920990047581
Ciphertext:
c: 15537860445392860627791921113547942268433746816211127779088849816425871267717435366808469771763672942339306019626033112604790279521256018388004503987281369444308463737059894900987688503037651823759352061264031327006538524035092808762774686406194114456168335939404457164139055755834030978327226465998086412320
Plaintext:
m': 34862844108815430278935886114814204661242105806196134451262421197958661737288465541172280522822644267285105893266043422314800759306377373320298160258654603531159702663926160107285223145666239673833817786345065431976764139550904726039902450456522584204556470321705267433321819673919640632299889369457498214445
insecure
```

#### solution code

```python
import random
import math
import secrets
from random import randrange

# 模N大数的幂乘的快速算法
def fastExpMod(b, e, m):  # 底数，幂，大数N
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0:
            e -= 1
            result = (result * b) % m
            continue
        e >>= 1
        b = (b * b) % m
    return result


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



# Generate a textbook RSA key pair
def create_keys(keyLength):
    p = get_big_prime(keyLength)
    q = get_big_prime(keyLength)
    n = p * q
    fn = (p - 1) * (q - 1)
    e = selectE(fn)
    d = match_d(e, fn)
    return n, e, d


# 随机在（1，fn）选择一个e，  满足gcd（e,fn）=1
def selectE(fn):
    while True:
        e = random.randint(0, fn)
        if math.gcd(e, fn) == 1:
            return e


# 根据e求出其逆元d
def match_d(e, fn):
    d = 0
    while True:
        if (e * d) % fn == 1:
            return d
        d += 1

# Given a plaintext message and a public key , return the encrypted message.
def encrypt(M, e, n):
    return fastExpMod(M, e, n)

# Given a ciphertext message and a private key , return the decrypted message.
def decrypt(C, d, m):
    return fastExpMod(C, d, m)


def encrypt_m(in_mess):
    c = ''
    for ch in in_mess:
        s = str(encrypt(ord(ch), e, n))
        c += s
    return c


def decrypt_m(in_cipher):
    p = ''
    for ch in in_cipher:
        c: str = str(decrypt(ord(ch), d, n))
        p += c
    return p


if __name__ == '__main__':
    # Read a decimal string representing a plaintext message.
    mess: str = input("input message:")
    # Raise an exception if m is invalid
    try:
        not mess.isdecimal()
    except ValueError:
        print('message is invalid')
    # Generate a textbook RSA key pair.
    n, e, d = create_keys(512)
    # Print the private key and the public key as multiple decimal strings.
    print("\nPrivate key：\nN:", n, " \nd:", d, )
    print("Public key ：\nN:", n, " \ne:", e, )
    # Encrypt the message . Print the encrypted message as a decimal string.
    cipher: str = encrypt_m(mess)
    print('Ciphertext:\nc:', cipher)
    # Decrypt the encrypted message . Print the decrypted message as a decimal string.
    message: str = decrypt_m(cipher)
    print('Plaintext:\nm:', message)
    print('insecure')



```


[Return Home](https://github.com/timerring/cryptography-codebase)
