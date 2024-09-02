import time
f = open("D:\Program Files\Python\测试.txt", "r", encoding="UTF-8")
print(type(f))
# print(f"读取10字节的结果:{f.read(10)}")
# print(f"{f.read()}")

for line in f:
    print(f"{line}")

with open("D:\Program Files\Python\测试.txt") as f:
    f.readlins()
    for line in f:
        print(f"{line}")