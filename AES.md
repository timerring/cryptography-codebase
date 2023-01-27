### Program : AES

**Modes of operations** allow you to encrypt more data than the block size of your symmetric block cipher. Example: `CBC`.

In this program, you are required to demonstrate the `AES-256-CBC` algorithm **with a third-party crypto library**, `pycryptodome`. Recall that you must provide a corresponding `requirements.txt` file if any third party libraries are involved in the code.

Your program does the following:

- Read a text string from the console input.
- Encode the text string with `utf-8` encoding, as the plaintext bytes.
- Pad the plaintext bytes with `pkcs7` algorithm.
- Print the padded bytes as a hex string.
- Read a Base64 string from the console input. The string represents the key bytes as a Base64 string. If the length of key bytes is not expected, abort the program with a Python code `raise Exception('key length mismatch')`
- Read a Base64 string from the console input. The string represents the IV bytes as a Base64 string. If the length of IV bytes is not expected, abort the program with a Python code `raise Exception('IV length mismatch')`
- Encrypt the padded plaintext bytes with the key and IV.
- Print the ciphertext bytes as a Base64 string.
- Decrypt the ciphertext bytes with the key and IV.
- Unpad the decrypted plaintext bytes with `pkcs7` algorithm.
- Print the unpadded bytes as a hex string.
- Decode the unpadded bytes with `utf-8` encoding, and print the decoded text string.

#### Example Input & Output

Input:

```txt
I don't like deadbeef. 你呢？
1UO7ZnmwcT7KtScS2hAZV+aZ1Gk95HPK1EqcXT6rqoU=
6GXIzJ0GD/76WkTtgmaDYQ==
```

Output:

```txt
4920646f6e2774206c696b652064656164626565662e20e4bda0e591a2efbc9f10101010101010101010101010101010
c0LWy2BUg949eMO+G8NgxUzKVNNFys8EzavYFhP0Tc/mZM/UVVe4E3b34cEyu1Ze
not identical
4920646f6e2774206c696b652064656164626565662e20e4bda0e591a2efbc9f
I don't like deadbeef. 你呢？
```

Note: the first line of the example input is consisting of the following 26 characters:

| I    |      | d    | o    | n    | '    | t    |      | l    | i    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| k    | e    |      | d    | e    | a    | d    | b    | e    | e    |
| f    | .    |      | 你   | 呢   | ？   |      |      |      |      |

#### solution code

```python
from Crypto.Cipher import AES
import base64


class PrpCrypt(object):

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC

    # pkcs7填充函数：
    @staticmethod
    def pkcs7_padding(in_bytes: str):
        pad_len: int = 16 - len(in_bytes) % 16
        if pad_len == 0:
            pad_len = 16
        in_str: str = str(in_bytes) + str(hex(pad_len) * pad_len).replace('0x', '')
        return in_str

    # pkcs7反填充函数：
    @staticmethod
    def pkcs7_unpadding(in_hex_str: str) -> str:
        end_str: str = in_hex_str[-2:]
        if end_str == '01':
            end_str: str = in_hex_str[0:-2]
        else:
            num: int = int(end_str[-2:], 16)
            end_str: str = in_hex_str[0:-(2 * num)]
        return end_str

    # AES加密函数：
    def encrypt(self, text: bytes):
        # Encrypt the padded plaintext bytes with the key and IV.
        ciphertext = AES.new(self.key, self.mode, self.iv)
        output_bytes: bytes = ciphertext.encrypt(bytes(text))
        return output_bytes

    # AES解密函数：
    def decrypt(self, text: bytes):
        plaintext = AES.new(self.key, self.mode, self.iv)
        output_bytes = plaintext.decrypt(bytes(text))
        return output_bytes


if __name__ == '__main__':
    # Read a text string from the console input.
    p_str: str = input('plaintext input:')
    # Read a Base64 string from the console input.
    key_b64: str = input('key input:')
    key: bytes = base64.b64decode(key_b64)
    IV_b64: str = input('IV input:')
    IV: bytes = base64.b64decode(IV_b64)

    # 异常处理函数：
    def judge(bytes_1: bytes, bytes_2: bytes):
        if len(bytes_1) % 24 != 0:
            if len(bytes_1) % 16 != 0:
                raise Exception('key length mismatch')
        if len(bytes_2) % 16 != 0:
            raise Exception('IV length mismatch ')
    judge(key, IV)
    pc = PrpCrypt(key, IV)  # 初始化密钥
    #  Encode the text string with utf-8 encoding, as the plaintext bytes.
    plaintext_str: str = p_str.encode('utf-8').hex()
    # Print the padded bytes as a hex string.
    print(pc.pkcs7_padding(plaintext_str))
    padded_plaintext: bytes = bytes.fromhex(pc.pkcs7_padding(plaintext_str))
    # Encrypt the padded plaintext bytes with the key and IV.
    ciphertext: str = base64.b64encode(pc.encrypt(padded_plaintext)).decode('utf-8')
    # Print the ciphertext bytes as a Base64 string.
    print(ciphertext)
    # Decrypt the ciphertext bytes with the key and IV.
    ciphertext_bytes: bytes = bytes.fromhex(base64.b64decode(ciphertext).hex())
    plaintext: str = base64.b64encode(pc.decrypt(ciphertext_bytes)).decode('utf-8')
    if base64.b64decode(plaintext).hex() == ciphertext:
        print('identical')
    else:
        print('not identical')
    # Print the unpadded bytes as a hex string.
    print(pc.pkcs7_unpadding(base64.b64decode(plaintext).hex()))
    # Decode the unpadded bytes with utf-8 encoding, and print the decoded text string.
    text_str: str = pc.pkcs7_unpadding(base64.b64decode(plaintext).hex())
    text_string: str = bytes.fromhex(text_str).decode('utf-8')
    print(text_string)
```


#### output

```txt
plaintext input:I don't like deadbeef. 你呢？
key input:1UO7ZnmwcT7KtScS2hAZV+aZ1Gk95HPK1EqcXT6rqoU=
IV input:6GXIzJ0GD/76WkTtgmaDYQ==
4920646f6e2774206c696b652064656164626565662e20e4bda0e591a2efbc9f10101010101010101010101010101010
c0LWy2BUg949eMO+G8NgxUzKVNNFys8EzavYFhP0Tc/mZM/UVVe4E3b34cEyu1Ze
not identical
4920646f6e2774206c696b652064656164626565662e20e4bda0e591a2efbc9f
I don't like deadbeef. 你呢？

进程已结束，退出代码为 0
```
![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127185440239.png)



[Return Home](https://github.com/timerring/cryptography-codebase)
