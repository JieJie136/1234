import random
num = random.randint(1, 10)
money = 10000
for i in range(1, 21):
    if num < 5:
        print(f"员工{i}绩效{num}, 不满足，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}, 发工资1000, 账户余额{money}")
    else:
        print(f"余额不足，当前余额{money}, 不发工资了")
        break