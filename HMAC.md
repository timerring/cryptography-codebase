### Program : HMAC

In this program, you are required to invoke the `scrypt` algorithms that are implemented in `hashlib` build-in library. Your program does the following:

- Read the plaintext password as a text string
- Encode the password into byte array, with `utf-8` encoding
- Read the salt byte array as a hex string
- Invoke the `scrypt` method with parameters $n=4$, $r=8$, $p=16$
- Output the result byte array as a hex string

**Example Input**

```txt
Thi$ i$ my passw0rd!
477d15cb740ca1da08f6d851361b3c80
```

**Example Output**

```txt
fd5963b9e6905d36ca8d00e3a740a3ab7a40b3d60237b6f2ed3025eee770f2d71bc95ba3e98265bea4308250d02f0e10bb78e710d9f0ef7ae9a4fa52a0818d27
```
#### solution code

```python
import hashlib
import base64

# define the function decode_utf8
def decode_utf8(in_bytes: bytes) -> str:
    return in_bytes.decode('utf-8')
#

 Read the plaintext password as a text string
password_str: str = input("input the plaintext password：")
# Encode the password into byte array, with utf-8 encoding
password_bytes: bytes = password_str.encode("utf-8")
# Read the salt byte array as a hex string
salt_str: str = input("input the salt：")
salt_bytes: bytes = bytes.fromhex(salt_str)
# Invoke the scrypt method with parameters n = 4 ,r = 8 ,p = 16
n: int = 4
r: int = 8
p: int = 16
result_bytes: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
# Output the result byte array as a hex string
result_str: str = result_bytes.hex()
print(result_str)
```

#### output

```txt
input the plaintext password：Thi$ i$ my passw0rd!
input the salt：477d15cb740ca1da08f6d851361b3c80
fd5963b9e6905d36ca8d00e3a740a3ab7a40b3d60237b6f2ed3025eee770f2d71bc95ba3e98265bea4308250d02f0e10bb78e710d9f0ef7ae9a4fa52a0818d27

进程已结束，退出代码为 0
```

A screenshot of the console output of the program
![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127185302658.png)



[Return Home](https://github.com/timerring/cryptography-codebase)
