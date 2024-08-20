
"""
字面量 被写在代码中固定的量
常用的字面量类型：整数、浮点数、字符串（双引号包围起来）
注释：单个与片段注释
print（）打印出来
print("hi") # print("wer"）打印不出来后面的,是注释
变量
直接print输出字面量数据类型 print(type("qwer"))
用变量存储type()结果  sty_type = type("qw"),  print(sty_type)
查看变量中存储的数据类型 name = "as" ,name_type = type(name), print(name_type)
变量无类型，存储是数据有类型
数据类型转换：int() float() str() 整形 浮点型 字符串，任何都可以转字符串，但是字符串里面的是数字才能转浮点型和整形，浮点数转整数会丢失小数部分
标识符：英文、数字、下划线，数字不能用在开头，注意规范
算数运算符：+（加）、-（减）、*（乘）、/（除）、//（除法取整）、%（取余）、**（指数乘法）
赋值运算符：=、-=、+=、/=、%=、**=、//=
字符串：单引号、双引号、三引号，可以用嵌套引号的方式打印出字符串 name = '\'wer\'',print(name)
字符串拼接:”字面量“ + ”字面量“，只能字符串本身，不能与数字拼接
字符串格式化：qwe = "yui %s" % name,%占位，s把变量变成字符串放入占位地方，
message = "北京%s, 工资%s" % (as,df)
%s转为字符串，%d转为整数，%f转为浮点型

数字精度控制：m.n，m控制宽度，.n控制小数点位数
%5d,如果数字不足5位，会自动在其左边用空格补足  %5.2f总共5位，小数部分占2位，小数点占1位

快速格式化：f"我是{}"快速格式化填充，不限数据类型，不控制精度
表达式也可以直接格式化：print("1 * 1 = %d" % (1 * 1)) \print(f"1 * 2 = {1 * 2}")
"""
