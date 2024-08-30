"""

name = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
new = []
index = 0
while index < len(name):
    element = name[index]
    if element % 2 == 0:
        new.append(element)
        index += 1
        print(f"新列表为：{new}")
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = []
for element in my_list:
    if element % 2 == 0:
        list1.append(element)
print(f"新列表：{list1}")

