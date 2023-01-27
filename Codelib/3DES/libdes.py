#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ['DES_Encrypt', 'DES_Decrypt']

# Reference: http://www.cnblogs.com/lixiaoxu/articles/7736917.html

def _permutationPC1(input64):
    pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44,
           36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12,
           4]
    ret56 = [0] * 56
    for i in range(56):
        ret56[i] = input64[pc1[i] - 1]
    return ret56


def _permutationPC2(input56):
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    ret48 = [0] * 48
    for i in range(48):
        ret48[i] = input56[pc2[i] - 1]
    return ret48


def _permutationIP(input64):
    ip = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
    ret64 = [0] * 64
    for i in range(64):
        ret64[i] = input64[ip[i] - 1]
    return ret64


def _permutationIP1(input64):
    ip1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13,
           53, 21, 61,
           29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41,
           9, 49, 17, 57, 25]
    ret64 = [0] * 64
    for i in range(64):
        ret64[i] = input64[ip1[i] - 1]
    return ret64


def _eBitSelection(input32):
    e = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16,
         17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    ret48 = [0] * 48
    for i in range(48):
        ret48[i] = input32[e[i] - 1]
    return ret48


def _permutationP(input32):
    p = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31,
         10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    ret32 = [0] * 32
    for i in range(32):
        ret32[i] = input32[p[i] - 1]
    return ret32


def _s1(input6):
    s1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3,
          8, 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s1[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s2(input6):
    s2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11,
          5, 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s2[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s3(input6):
    s3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15,
          1, 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s3[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s4(input6):
    s4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14,
          9, 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s4[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s5(input6):
    s5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8,
          6, 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s5[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s6(input6):
    s6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3,
          8, 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s6[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s7(input6):
    s7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8,
          6, 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s7[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _s8(input6):
    s8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9,
          2, 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ret4 = [0] * 4
    i = input6[0] * 2 + input6[5] * 1
    j = input6[1] * 8 + input6[2] * 4 + input6[3] * 2 + input6[4] * 1
    retBase10 = s8[i * 16 + j]

    ret4[3] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[2] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[1] = retBase10 % 2
    retBase10 = retBase10 // 2
    ret4[0] = retBase10 % 2

    return ret4


def _left1(input28):
    l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
         17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 1]
    ret28 = [0] * 28
    for i in range(28):
        ret28[i] = input28[l[i] - 1]
    return ret28


def _right1(input28):
    l = [28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
         17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    ret28 = [0] * 28
    for i in range(28):
        ret28[i] = input28[l[i] - 1]
    return ret28


def _leftRound(input28, roundID):
    c = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(c[roundID]):
        input28 = _left1(input28)
    return input28


def _rightRound(input28, roundID):
    c = [0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for i in range(c[roundID]):
        input28 = _right1(input28)
    return input28


def _xor(inputA, inputB):
    assert len(inputA) == len(inputB)

    ret = [0] * len(inputA)
    for i in range(len(inputA)):
        ret[i] = 0 if inputA[i] == inputB[i] else 1
    return ret


def _f(input32, key48):
    input48 = _eBitSelection(input32)
    ret48 = _xor(input48, key48)
    ret32 = _s1(ret48[0:6]) + _s2(ret48[6:12]) + _s3(ret48[12:18]) + _s4(ret48[18:24]) + \
            _s5(ret48[24:30]) + _s6(ret48[30:36]) + _s7(ret48[36:42]) + _s8(ret48[42:])
    ret32 = _permutationP(ret32)

    return ret32


def _des(input64, key64, encOrDec):
    assert encOrDec in ['encrypt', 'decrypt']
    input64 = _permutationIP(input64)
    inputLeft32 = input64[0:32]
    inputRight32 = input64[32:]

    key56 = _permutationPC1(key64)
    keyLeft28 = key56[0:28]
    keyRight28 = key56[28:]

    for i in range(16):
        if encOrDec == 'decrypt':
            keyLeft28 = _rightRound(keyLeft28, i)
            keyRight28 = _rightRound(keyRight28, i)
        elif encOrDec == 'encrypt':
            keyLeft28 = _leftRound(keyLeft28, i)
            keyRight28 = _leftRound(keyRight28, i)
        else:
            assert False

        newKey48 = _permutationPC2(keyLeft28 + keyRight28)

        inputLeft32, inputRight32 = inputRight32, _xor(inputLeft32, _f(inputRight32, newKey48))

    inputLeft32, inputRight32 = inputRight32, inputLeft32
    return _permutationIP1(inputLeft32 + inputRight32)


def _binListFromInt(input):
    ret64 = [0] * 64
    for i in range(64):
        ret64[63 - i] = input % 2
        input = input // 2
    return ret64


def _intFromBinList(input):
    n = 0
    base = 1
    for i in range(len(input)):
        n += input[len(input) - i - 1] * base
        base *= 2
    return n


def DES_Encrypt(plaintext: bytes, key: bytes) -> bytes:
    if len(plaintext) != 8 or len(key) != 8:
        raise Exception('Argument length mismatch.')

    plaintextInt = int.from_bytes(plaintext, byteorder='big', signed=False)
    keyInt = int.from_bytes(key, byteorder='big', signed=False)
    resultBinList = _des(_binListFromInt(plaintextInt), _binListFromInt(keyInt), 'encrypt')
    assert len(resultBinList) % 8 == 0
    return int.to_bytes(_intFromBinList(resultBinList), length=len(resultBinList) // 8, byteorder='big', signed=False)


def DES_Decrypt(ciphertext: bytes, key: bytes) -> bytes:
    if len(ciphertext) != 8 or len(key) != 8:
        raise Exception('Argument length mismatch.')

    ciphertextInt = int.from_bytes(ciphertext, byteorder='big', signed=False)
    keyInt = int.from_bytes(key, byteorder='big', signed=False)
    resultBinList = _des(_binListFromInt(ciphertextInt), _binListFromInt(keyInt), 'decrypt')
    assert len(resultBinList) % 8 == 0
    return int.to_bytes(_intFromBinList(resultBinList), length=len(resultBinList) // 8, byteorder='big', signed=False)
