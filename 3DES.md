### Program : 3DES

In this program, you are required to implement the 3DES algorithm using the provided encrypt and decrypt function of DES. The encrypt and decrypt method of 3DES should also be pure functions, i.e. without side effects.

Your program does the following:

- Read a hex string from the console input. The string represents the plaintext bytes as a hex string.

- Read a hex string from the console input. The string represents the first key bytes as a hex string.

- Read a hex string from the console input. The string represents the second key bytes as a hex string.

- Read a hex string from the console input. The string represents the third key bytes as a hex string.

- Encrypt the plaintext with the three keys.

- Print the ciphertext bytes as a hex string.

- Decrypt the ciphertext with the three keys.

- Print the plaintext bytes after decryption as a hex string.

#### Example Input & Output

Input:

```txt
8787878787878787
133457799bbcdff1
0e329232ea6d0d73
133457799bbcdff1
```

Output:

```txt
e98a0b8e59b3eeb7
8787878787878787
```

#### solution code
```python
from libdes import DES_Encrypt, DES_Decrypt


def validate_des_key(key: bytes) -> bool:
    for keyByte in key:
        binStr: str = "{0:0>8b}".format(keyByte)
        if sum([1 if b == '1' else 0 for b in binStr]) % 2 == 0:
            return False
    return True


if __name__ == '__main__':
    plaintextHex: str = input('plaintext:')
    key1Hex: str = input('key1:')
    if not validate_des_key(bytes.fromhex(key1Hex)):
        raise Exception('Parity check failed on the key.')
    key2Hex: str = input('key2:')
    if not validate_des_key(bytes.fromhex(key2Hex)):
        raise Exception('Parity check failed on the key.')
    key3Hex: str = input('key3:')
    if not validate_des_key(bytes.fromhex(key3Hex)):
        raise Exception('Parity check failed on the key.')

    ciphertext1: bytes = DES_Encrypt(
        bytes.fromhex(plaintextHex),
        bytes.fromhex(key1Hex),
    )

    ciphertext2: bytes = DES_Decrypt(
        ciphertext1,
        bytes.fromhex(key2Hex),
    )

    ciphertext3: bytes = DES_Encrypt(
        ciphertext2,
        bytes.fromhex(key3Hex),
    )

    print('ciphertext:', ciphertext3.hex())

    plaintext3: bytes = DES_Decrypt(
        ciphertext3,
        bytes.fromhex(key3Hex),
    )

    plaintext2: bytes = DES_Encrypt(
        plaintext3,
        bytes.fromhex(key2Hex),
    )

    plaintext1: bytes = DES_Decrypt(
        plaintext2,
        bytes.fromhex(key1Hex),
    )

    print('plaintext:', plaintext1.hex())


```
#### output
```txt
plaintext:8787878787878787
key1:133457799bbcdff1
key2:0e329232ea6d0d73
key3:133457799bbcdff1
ciphertext: e98a0b8e59b3eeb7
plaintext: 8787878787878787

进程已结束，退出代码为 0
```


[Return Home](https://github.com/timerring/cryptography-codebase)
