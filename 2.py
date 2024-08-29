
"""
字面量 被写在代码中固定的量，写在print中的语句
常用的字面量类型：整数、浮点数、字符串（双引号包围起来）

注释：单个与片段注释
print（）打印出来,print中用逗号分隔输出多个变量出来
print("hi") # print("wer"）打印不出来后面的,是注释

变量
直接print输出字面量数据类型 print(type("qwer"))
用变量存储type()结果  sty_type = type("qw"),  print(sty_type)
查看变量中存储的数据类型 name = "as" ,name_type = type(name), print(name_type)(和上面一种本质一样的）
变量无类型，存储的数据有类型

数据类型转换：int() float() str() 整形 浮点型 字符串，任何都可以转字符串，但是字符串里面的是数字才能转浮点型和整形，浮点数转整数会丢失小数部分
标识符：英文、数字、下划线，数字不能用在开头，注意规范

算数运算符：+（加）、-（减）、*（乘）、/（除）、//（除法取整）、%（取余）、**（指数乘法）
赋值运算符：=、-=、+=、/=、%=、**=、//=

字符串：单引号、双引号、三引号，可以用嵌套引号的方式打印出字符串name = " 'qwe' "(这就是一个包含单引号的字符串)，\'表示单引号，print(" \'wer\' ") = 'wer'
字符串拼接:”字面量“ + ”字面量“或者”字面量“ + ”变量“。只能字符串本身，不能与数字拼接
字符串格式化：qwe = "yui %s" % name,%占位，s把变量变成字符串放入占位地方，
message = "北京%s, 工资%s" % (as,df),print(message)
%s转为字符串，%d转为整数，%f转为浮点型

数字精度控制：m.n，m控制宽度，.n控制小数点位数
%5d,如果数字不足5位，会自动在其左边用空格补足  %5.2f总共5位，小数部分占2位，小数点占1位

快速格式化：print(f"我是{}")快速格式化填充，不限数据类型，不控制精度
表达式也可以直接格式化：print("1 * 1 = %d" % (1 * 1)) 或者 print(f"1 * 2 = {1 * 2}")或者print("类型为%s" % type('字符串'))
简单print("每日增长系数是: %.1f, 经过%d天的增长后, 股价到达了%5.2f" % (stock_price_daily_growth_factor,
                            growth_days, stock_price * stock_price_daily_growth_factor ** growth_days)),这里要记住
input()输入数据，input("aaaaa")可以提前打印一点信息,默认输入的都是字符串，使用时候自行转换数据类型
int(input("请输入你的学号))
布尔类型：True和 False 比较运算符> < >= <= == !=,这6个符号的结果只有True和False

判断：if elif else,注意嵌套
\t是对齐，end=''表示在字符串结尾不是添加换行符，而是一个空字符，类似于分开，print()换行, \n换行

while 条件。条件满足时候就会不断循环。

for 变量 in 待处理的数据集,
range()得到一个数字序列，range(5)得到[0，1，2，3，4],range(4,6)=[4,5]不包括右边

continue中断本次循环，后面语句也不管，直接开始一次新循环。只能影响最近的一次for循环，其他for循环管不到
break直接把它所在最近的整个循环都结束，跳到外面，其他的for循环影响不了

函数：def add(x, y):
    result = x + y
    return result
r = add(5, 6)
print(r)   我们调用add()函数，同时通过return把结果返回传出去给我们定义的变量r，函数体中在return后面的代码根本不执行

none是个特殊的字面量，
函数的嵌套调用，直接在函数a中写函数b的名称，然后等函数b调用玩之后才会接着调用函数a的内容

局部变量：在函数体内调用的变量，函数体外无法使用
全局变量：在函数体内部和外部都可以调用
global把函数体内部的局部变量声明为全局变量

数据容器：一种可以容纳多份数据的数据类型，容纳的每一个数据称为一个元素，每个元素可以是任意类型的数据。
容器类型：列表、元组、字符串、集合、字典。

列表：my_list = [元素1， 元素2，。。。]
"""
