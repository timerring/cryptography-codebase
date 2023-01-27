import hashlib
import base64


# define the function decode_utf8
def decode_utf8(in_bytes: bytes) -> str:
    return in_bytes.decode('utf-8')


# Program 1: Regular hash algorithms

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

# Program 2: HMAC

# Read the plaintext password as a text string
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
