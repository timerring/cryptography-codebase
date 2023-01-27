完成一个 Python 程序，实现密码存储和验证，用于模拟身份验证服务器，以便破解数据库的对手无法获得用户的明文密码。实现基本的注册和登录功能。

测试样例如下：

#### input

```txt
R
timerring
i love cryptography
L
timerring
i love cryptography
L
timerring
i love cipher
L
Who
i love cryptography
Q
```

该系统的源码如下：
#### source code

```python
from __future__ import annotations
from typing import Dict
import getpass
import hashlib
import os

database: Dict[str, UserPassword] = dict()


class UserPassword:
    def __init__(self, in_username, in_password_hash, in_salt):
        self.username: str = in_username
        self.password_hash: bytes = in_password_hash
        self.salt: bytes = in_salt
        self.method: str = 'scrypt'

    # define verify_password function
    def verify_password(self, password: str) -> bool:
        password_ver: bytes = password.encode("utf-8")
        # use the same salt
        salt_ver: bytes = self.salt
        # set corresponding parameters
        n: int = 4
        r: int = 8
        p: int = 16
        password_hash_ver: bytes = hashlib.scrypt(password_ver, salt=salt_ver, n=n, r=r, p=p)
        # verify the hash value of the password
        if password_hash_ver == self.password_hash:
            return True
        else:
            return False


def database_add_item(user: UserPassword) -> None:
    if user.username in database:
        raise Exception('User {} already exists.'.format(user.username))
    database[user.username] = user


def login_user(username: str, password_plaintext: str) -> bool:
    if username not in database:
        raise Exception('User {} does not exist.'.format(username))
    return database[username].verify_password(password_plaintext)


def register_user(username: str, password_plaintext: str) -> None:
    password_bytes: bytes = password_plaintext.encode("utf-8")
    # The os.urandom function is used to obtain random bytes of a specified length
    # generate the salt bytes
    salt_bytes: bytes = os.urandom(64)
    # set corresponding parameters
    n: int = 4
    r: int = 8
    p: int = 16
    # Hash encryption
    password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=n, r=r, p=p)
    # construct instance object
    User: UserPassword = UserPassword(username, password_hash, salt_bytes)
    # Add to database
    database_add_item(User)


if __name__ == '__main__':
    while True:
        try:
            print('Usage:')
            print('\tR - register a new user')
            print('\tL - login with an existing user')
            print('\tQ - exit')
            print('')
            command: str = input('Input command:')
            if command == 'Q':
                exit(0)
            elif command == 'R' or command == 'L':
                username: str = input('Input username:')
                # password: str = getpass.getpass('Input password:') # will not work properly for PyCharm, IDLE, etc.
                password: str = input('Input password:')
                if command == 'R':
                    register_user(username, password)
                    print('User created successfully.')
                elif command == 'L':
                    login_valid: bool = login_user(username, password)
                    if login_valid:
                        print('User logged in successfully.')
                    else:
                        print('Password verification failed. Can not logged in.')
                else:
                    assert False
            else:
                raise Exception('Invalid command.')
        except Exception as e:
            print('Error: {}'.format(e))

```

#### output

```txt
Usage:
	R - register a new user
	L - login with an existing user
	Q - exit

Input command:R
Input username:timerring
Input password:i love cryptography
User created successfully.
Usage:
	R - register a new user
	L - login with an existing user
	Q - exit

Input command:L
Input username:timerring
Input password:i love cryptography
User logged in successfully.
Usage:
	R - register a new user
	L - login with an existing user
	Q - exit

Input command:L
Input username:timerring
Input password:i love cipher
Password verification failed. Can not logged in.
Usage:
	R - register a new user
	L - login with an existing user
	Q - exit

Input command:L
Input username:Who
Input password:i love cryptography
Error: User Who does not exist.
Usage:
	R - register a new user
	L - login with an existing user
	Q - exit

Input command:Q

进程已结束，退出代码为 0

```
由输出可知，系统功能一切正常。



[Return Home](https://github.com/timerring/cryptography-codebase)
