import math

key = input('please enter the key：')


# 加密
def encryptMessage(msg):
    cipher = ""

    k_index = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # 计算列数
    col = len(key)

    # 计算最大行
    row = int(math.ceil(msg_len / col))

    # 将空白处用'_'填充
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # 按行填充字符
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    # 重排顺序形成密文
    for _ in range(col):
        curr_idx = key.index(key_lst[k_index])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_index += 1

    return cipher


# 解密过程
def decryptMessage(cipher):
    msg = ""

    k_index = 0

    msg_index = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)

    # 计算列数
    col = len(key)

    # 求出最大行数
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))

    # 创建新矩阵储存解密出的明文
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    # 按列重排矩阵
    for _ in range(col):
        curr_idx = key.index(key_lst[k_index])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_index]
            msg_index += 1
        k_index += 1

    # 转换为字符串输出
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg


msg = input('请输入加密的内容：')

cipher = encryptMessage(msg)
print("密文为: {}".
      format(cipher))

print("明文为: {}".
      format(decryptMessage(cipher)))