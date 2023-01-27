### Program : Regular hash algorithms

In this program, you are required to invoke the `md5` and `sha256` algorithms that are implemented in `hashlib` build-in library. Your program does the following:

- Read the input byte array as a hex string.
- Output the md5 digest of the input, as a hex string.
- Output the md5 digest of the input, as a Base64 string.
- Output the sha256 digest of the input, as a hex string.
- Output the sha256 digest of the input, as a Base64 string..

**Example Input 1**

```txt
d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70
```

**Example Output 1**

```txt
MD5 digest of the input:
79054025255fb1a26e4bc422aef54eb4
eQVAJSVfsaJuS8QirvVOtA==

SHA256 digest of the input:
8d12236e5c4ed9f4e790db4d868fd5c399df267e18ff65c1107c328228cffc98
jRIjblxO2fTnkNtNho/Vw5nfJn4Y/2XBEHwygijP/Jg=
```

**Example Input 2**

```txt
d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70
```

**Example Output 2**

```txt
MD5 digest of the input:
79054025255fb1a26e4bc422aef54eb4
eQVAJSVfsaJuS8QirvVOtA==

SHA256 digest of the input:
b9fef2a8fc93b05e7701e97196fda6c4fbeea25ff8e64fdfee7015eca8fa617d
uf7yqPyTsF53Aelxlv2mxPvuol/45k/f7nAV7Kj6YX0=
```

#### solution code
```python
import hashlib
import base64


# define the function decode_utf8
def decode_utf8(in_bytes: bytes) -> str:
    return in_bytes.decode('utf-8')


# Program: Regular hash algorithms

string_1: str = input("input the message：")
# Read the input byte array as a hex string.
message_1: bytes = bytes.fromhex(string_1)
# Output the md5 digest of the input, as a hex string.
hash1_hex: str = hashlib.md5(message_1).hexdigest()
# Output the md5 digest of the input, as a Base64 string.
hash1_bytes: bytes = hashlib.md5(message_1).digest()
hash1_base64: str = base64.b64encode(hash1_bytes).decode('utf-8')
print('MD5 digest of the input:')
print(hash1_hex)
print(hash1_base64)

# Output the sha256 digest of the input, as a hex string.
hash2_hex: str = hashlib.sha256(message_1).hexdigest()
# Output the sha256 digest of the input, as a Base64 string.
hash2_bytes: bytes = hashlib.sha256(message_1).digest()
hash2_base64: str = base64.b64encode(hash2_bytes).decode('utf-8')
print('\nSHA256 digest of the input:')
print(hash2_hex)
print(hash2_base64)
```

#### output

```txt
input the message：d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70
MD5 digest of the input:
79054025255fb1a26e4bc422aef54eb4
eQVAJSVfsaJuS8QirvVOtA==

SHA256 digest of the input:
8d12236e5c4ed9f4e790db4d868fd5c399df267e18ff65c1107c328228cffc98
jRIjblxO2fTnkNtNho/Vw5nfJn4Y/2XBEHwygijP/Jg=

进程已结束，退出代码为 0

input the message：d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70
MD5 digest of the input:
79054025255fb1a26e4bc422aef54eb4
eQVAJSVfsaJuS8QirvVOtA==

SHA256 digest of the input:
b9fef2a8fc93b05e7701e97196fda6c4fbeea25ff8e64fdfee7015eca8fa617d
uf7yqPyTsF53Aelxlv2mxPvuol/45k/f7nAV7Kj6YX0=

进程已结束，退出代码为 0
```

A screenshot of the console output of the program
![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127184603994.png)
![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127184632994.png)



[Return Home](https://github.com/timerring/cryptography-codebase)
