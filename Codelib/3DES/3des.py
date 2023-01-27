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

