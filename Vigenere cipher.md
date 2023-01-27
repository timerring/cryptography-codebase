
### Program: Vigenère cipher (on alphabet string)

In this program, you are required to implement the Vigenère cipher algorithm from scratch, to encrypt and decrypt for alphabet string. The encrypt and decrypt method should be pure functions, i.e. without side effects.

Your program does the following:

- Read an alphabet string from the console input, where the string is only consisting of 26 uppercase letters (A-Z). The first string represents the plaintext.
- Read the second alphabet string. It is ensured that the length of second alphabet string is the same with the first string. The second string represents the key.
- Encrypt the plaintext with the key.
- Print the ciphertext alphabet string.
- Decrypt the ciphertext with the key.

#### Example Input & Output

Input:

```txt
ABCDEFG
ABCDEFG
```

Output:

```txt
ACEGIKM
ABCDEFG
```
#### solution code
```python
from string import ascii_uppercase as uppercase
from itertools import cycle

# 密码表
table = dict()
for ch in uppercase:
    index = uppercase.index(ch)
    table[ch] = uppercase[index:] + uppercase[:index]
# 解码表
deTable = {'A': 'A'}
start = 'Z'
for ch in uppercase[1:]:
    index = uppercase.index(ch)
    deTable[ch] = chr(ord(start) + 1 - index)


# 解密密钥
def deKey(key):
    return ''.join([deTable[i] for i in key])


# 加密/解密
def encrypt(plainText, key):
    result = []
    # 创建cycle对象，支持密钥字母的循环使用
    currentKey = cycle(key)
    for ch in plainText:
        if 'A' <= ch <= 'Z':
            index = uppercase.index(ch)
            # 获取密钥字母
            ck = next(currentKey)
            result.append(table[ck][index])
        else:
            result.append(ch)
    return ''.join(result)


# 加密过程
passage = input('请用大写字母输入加密的内容：')
key = input('请用大写字母输入密钥：')
ciphertext = encrypt(passage, key)
print('密文为：', ciphertext)
# 解密过程
key1 = key
print('解密后的内容为：', encrypt(ciphertext, deKey(key1)))
```
#### output

```python
请用大写字母输入加密的内容：ABCDEFG
请用大写字母输入密钥：ABCDEFG
密文为： ACEGIKM
解密后的内容为： ABCDEFG
```



[Return Home](https://github.com/timerring/cryptography-codebase)

