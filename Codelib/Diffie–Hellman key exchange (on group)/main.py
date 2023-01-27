import random

p: int = 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
alpha: int = 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729


# 快速模幂函数:
def quick_mod(in_a: int, in_b: int, in_p: int) -> int:
    in_a %= in_p  # 预处理
    ans = 1  # 记录结果
    while in_b != 0:
        if in_b & 1:
            ans = (ans * in_a) % in_p
        in_b >>= 1  # 移位操作
        in_a = (in_a * in_a) % in_p
    return ans


da: int = random.randint(1, p - 1)
pa: int = quick_mod(alpha, da, p)
print('Alice to Bob:', pa)

db: int = random.randint(1, p - 1)
pb: int = quick_mod(alpha, db, p)
print('Bob to Alice:', pb)

k_Alice: int = quick_mod(pb, da, p)
print('Result (Alice view):', k_Alice)

k_Bob: int = quick_mod(pa, db, p)
print('Result (Bob view):', k_Bob)
