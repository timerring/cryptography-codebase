### Program : Type Hint, String, Bytes, Hex, Base64

In this program, you are required to learn basic concepts of Python 3.

Type hints is a feature to specify the type of a variable, which is useful for write correct codes. In all lab assignments, you are **required** to write Python 3 code with type hints feature. Recall that you are required to use **at least** Python 3.10, otherwise you might suffer from issues brings by type hints as PEP 563 has not become the default option until Python 3.10.

Your programs does the following:

- Read a byte array from the console input, where the byte array is expressed as a hex string (`str`). The console input is:

  ```txt
  deadbeef
  ```

- Decode the hex string as the byte array (`bytes`)

- Print each byte in the byte array as a decimal integer, with a space as the separator, i.e.:

  ```python
  def output_bytes(in_bytes:bytes):
      for ch in in_bytes:
          print(ch, end=' ')
      print()
  ```

- Print each byte in the byte array as a hexadecimal integer, with a space as the separator

- Encode the byte array as a Base64 string(`str`), and output the string

- Read another byte array from the console input, where the byte array is expressed as a hex string (`str`). The console input is:

  ```txt
  6465616462656566
  ```

- Decode the hex string as the byte array (`bytes`)

- As the decoded byte array **happens to be** a UTF-8 (or, ASCII) encoded bytes, decode the byte array to the text string(`str`):

  ```python
  def decode_utf8(in_bytes:bytes)->str:
      return in_bytes.decode('utf-8')
  ```

- Print the decoded text string

In your `readme.pdf` file, apart from the general information, it should include:

- A figure representing the relationship between all the variables in your program with type `bytes` and `str`. Example here:

![](https://img-blog.csdnimg.cn/img_convert/ee5a78e3285f30181f368782128004b2.png)

  The figure above is corresponding to the following code.

  ```python
  first_hex:str = input()
  first_bytes:bytes = bytes.fromhex(first_hex)
  ```

#### solution code
```python
import base64


def output_bytes(in_bytes: bytes):
    for ch in in_bytes:
        print(ch, end=' ')
    print()


def output_hex(in_bytes: bytes):
    for ch in in_bytes:
        print(hex(ch), end=' ')
    print()


def decode_utf8(in_bytes: bytes) -> str:
    return in_bytes.decode('utf-8')


print("Enter a string str1:")
str1: str = input()
byte_array: bytes = bytearray.fromhex(str1)
output_bytes(byte_array)
output_hex(byte_array)
encoded: bytes = base64.b64encode(byte_array)
print(encoded)
print("Enter a string str2:")
str2: str = input()
byte_array2: bytes = bytearray.fromhex(str2)
str3: str = decode_utf8(byte_array2)
print(str3)
```
+ output

```python
Enter a string str1:
deadbeef
222 173 190 239 
0xde 0xad 0xbe 0xef 
b'3q2+7w=='
Enter a string str2:
4445414442454546
DEADBEEF

进程已结束，退出代码为 0
```

+ operating system version：WIN10
+ CPU instruction set：x64
+ Python interpreter version：Python3.9
A screenshot of the console output of the program

![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127182923498.png)

A figure representing the relationship between all the variables in your program with type bytes and str：
![](https://raw.githubusercontent.com/timerring/picgo/master/picbed/image-20230127182939114.png)



[Return Home](https://github.com/timerring/cryptography-codebase)
