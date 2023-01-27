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


