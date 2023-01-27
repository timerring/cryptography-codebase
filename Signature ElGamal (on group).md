### Program : ElGamal (on group)

In this part, you are required to implement the ElGamal algorithm for signing from scratch. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Same as Lab 04.
- Sign
  - Given a plaintext message $m \in \mathbb{F}_p$ and a private key $(p,\alpha,a)$, return the signature $(r,s)$.
- Verify
  - Given a plaintext message $m \in \mathbb{F}_p$, the signature $(r,s)$, and a public key $(p,\alpha,\beta)$, check whether the signature is valid or not.

Your program does the following:

- Generate a private key and the corresponding public key. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Sign the message $m$. Print the signature $(r,s)$ as multiple decimal string.
- Verify the signature $(r,s)$ of message $m$. Print `valid` if the signature is valid. Print `invalid` otherwise.
- Randomly pick a number as a faked message $m^\prime$, and verify the signature $(r,s)$ of message $m^\prime$. Print `valid` if the signature is valid. Print `invalid` otherwise.
- Randomly pick numbers as a faked signature $(r^\prime,s^\prime)$, and verify the signature $(r^\prime,s^\prime)$ of message $m$. Print `valid` if the signature is valid. Print `invalid` otherwise.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- finding a primitive root modulo prime p
- **Extended Euclidean Algorithm**

**Example Input & Output**

Input

```txt
4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
```

Output

```txt
Private Key:
p: 7623676177142273666176960941160763267715363061271226168423102803703307888568083070768414734233175022763592082166829461334117317633004076503299319393933531
alpha: 4852157426089893935411617364720859800493089641146556442371879299424783880014557103402720169349703681228223731146566716914079006206076028164786870639438634
a: 3378999248556716821986051126236329620786292051032565251155929677736759564488623249788309621451301313648501424873153999478194379023701985528788334198300666
Public Key:
p: 7623676177142273666176960941160763267715363061271226168423102803703307888568083070768414734233175022763592082166829461334117317633004076503299319393933531
alpha: 4852157426089893935411617364720859800493089641146556442371879299424783880014557103402720169349703681228223731146566716914079006206076028164786870639438634
beta: 900191922914835354062391486383477573543038624757518577920766087560733127924139275266000620349618745988286788581537670898557439116232221539792308522703996
Signature:
r: 6319172751757190059617527527206702628329370565289520380207782237638117089626184819108054497002450108714662052571938062244969670733303628072961698241980976
s: 4487722435787272797267428160768266252523442175017409508193970626399238483647311021229856082277095824456827558298764078442861955288380137538351154715433474
Verify (r,s) of m:
valid
m' (faked): 3794592956927179165727339787771495164761281462584199354337653233001069555811671313157589195265413704693831537814309912166154940955900923275208659567603551
Verify (r,s) of m':
invalid
r' (faked): 3159232051056019432416597255218241709553275595410987553313618304348446526218613835913933078438390905736100418385914557962667666159701449384865696308181869
s' (faked): 6724747854387400941199482927499544178640823360059844483666200355270210965256010155751083409193280897361331961705674904878262224584821396243969282511950802
Verify (r',s') of m:
invalid
```

#### solution code

```python
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

```

#### output

```python
input the plaintext:
41376968769300902675223986976535501934053116896640695743228346832131991265313482
63326633721504049779673544721298253021191958429503842792929508773630980912
Private Key:
 p:

9647662614618593612678349153450129210018062536440151968869493082833238167274143198466828697857688740203683581672378177270017851138691043400958875425601339
alpha:
 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042048
a:
 1352813006895829402637906374263634259803934423638555090889806068014955570897844166303338007635068708486142360302771143081413108034429460243147134733737820
Public Key:
 p:
 9647662614618593612678349153450129210018062536440151968869493082833238167274143198466828697857688740203683581672378177270017851138691043400958875425601339
alpha:
 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042048
beta:
 4943906246828233075173795708136103648075290537591704500749594060122083781980890611284388177471101296754799372666419925262713522300068537095831524801083735

Signature:
r:
 5211930128683273967454085849625600825658528457750135710392237348237036698204567961449042290886685311489671052965220963625931147217281336640040201481247092

s:
 9601075377199493365413948935734087520680845077662592726571219106328306551468632442874821664654801371707486921835129281406335251143534653201158634077578810
Verify (r,s) of m:
valid

m' (faked):
 13181484855944115180804852555915813304509338239496938457903967429525861251378248748288077599914310541295005029288105172018037308599021649523045336777613325
Verify s of m':
invalid

r' (faked):
 12362805104143777187285712880347281411565051141816790493197347445231574973456840246008991307448623235786896471440658633258439408545945664148515919220118187
s' (faked):
 5657512693194656903430242147504308401718061672376076433479350517650523404535715971127139643274326528707795141467127319987473710181998155732438536396140368
Verify s' of m:
invalid

进程已结束，退出代码为 0

```
A screenshot of the console output of the program：
![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127185015328.png)





[Return Home](https://github.com/timerring/cryptography-codebase)
