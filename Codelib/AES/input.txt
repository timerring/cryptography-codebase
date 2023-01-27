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