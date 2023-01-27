### Program: Columnar transposition (on alphabet string)

Reference：http://rumkin.com/tools/cipher/coltrans.php

A columnar transposition, also known as a row-column transpose, is a very simple cipher to perform by hand. First, you write your message in columns.  Then, you just rearrange the columns.  For example.  I have the message, `Which wristwatches are swiss wristwatches`.  You convert everything to upper case and write it without spaces.  When you write it down, make sure to put it into columns and number them.  Let's use five columns.

|               | Unencoded     | Rearranged    |
| ------------- | ------------- | ------------- |
| **Column #:** | **4 2 5 3 1** | **1 2 3 4 5** |
|               | W H I C H     | H H C W I     |
|               | W R I S T     | T R S W I     |
|               | W A T C H     | H A C W T     |
|               | E S A R E     | E S R E A     |
|               | S W I S S     | S W S S I     |
|               | W R I S T     | T R S W I     |
|               | W A T C H     | H A C W T     |
|               | E S           | S E           |

Now, you just read the columns down in the order that you number them. Above, you will see the key is `4 2 5 3 1`, which means you write down the last column first, then the second, then the fourth, the first, and finally the middle.  When you are all done, you will get `HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT`. 

Your program does the following:

- Read an integer from the console, representing the column count. In the example above, the count is `5`.
- Read the encryption key, i.e. the order of columns, separated by space. In the example above, the key is `4 2 5 3 1`.
- Read the plaintext string in one line. In the example above, the plaintext is `WHICHWRISTWATCHESARESWISSWRISTWATCHES`.
- Perform the columnar transposition.
- Print the ciphertext string. In the example above, the ciphertext is `HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT`.

#### Example Input & Output

Input:

```txt
5
4 2 5 3 1
WHICHWRISTWATCHESARESWISSWRISTWATCHES
```

Output:

```txt
HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT
```

#### solution code
```python
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
```

#### output

```txt
please enter the key：42531
请输入加密的内容：WHICHWRISTWATCHESARESWISSWRISTWATCHES
密文为: HTHESTH_HRASWRASCSCRSSC_WWWESWWEIITAIIT_
明文为: WHICHWRISTWATCHESARESWISSWRISTWATCHES

进程已结束，退出代码为 0
```



[Return Home](https://github.com/timerring/cryptography-codebase)
