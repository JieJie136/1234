
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

列表：my_list = [元素1， 元素2，。。。]，元素之间可以是不同类型数据，同时列表则可以再嵌套一个列表
嵌套：lklist = [ [1,2,3], [2,3,4]]

下标索引（取出数据）：从前往后，下标0 1 2 3 ：从后往前，下标-1 -2 -3。取嵌套列表，两层索引就行，print(my_list[0][1])，不要超出数字范围
列表中有很多方法：跟函数相关。将函数定义为class类成员，就称之为方法

查询：查找指定元素在列表的下标。基本格式：列表.index（元素）
修改：列表名[下标] = 要修改的元素，下标可以是从前往后，也可以是从后往前
插入：列表.insert(下标，插入元素)
追加：列表.append(追加元素），将指定单个元素，添加到列表尾部。
追加多个元素：列表.extend(其他数据容器),将整个列表添加到末尾
删除：del 列表[下标]或者 列表.pop(下标)。使用pop方法的话，本质是把列表元素取出来，可以用变量接受这个元素
删除某个元素在列表中第一个匹配项：列表.remove(元素)。删除io。如果从前往后有3个io,只会删除第一个io，后面两个不会被删除。
清空整个列表：列表.clear()
统计某个元素在列表中的数量：列表.count(元素)
统计整个列表长度:len(列表)

遍历列表：while循环和for循环.
用列表[下标]的方式取出来，定义一个变量表示下标，从0开始。下标值《列表元素数量
for i in my_list:
    new.qppend(i)
print(f"{new}")

i = 0
while i in my_list:
    if i % 2 == 0:
    new.qppend(i)
print(f"{new}")

元组：大概类似于一个不可修改的列表。定义：变量 = (元素， 元素， 元素。。。)。各个元素可以是不同类型数据
定义空元组：变量 = （）， 变量 = tuple（）。如果定义的元组只有一个元素，要在其后面加个逗号，否则成字符串了。
元组可以嵌套：t5 = ((1, 2, 3 ), (4, 5, 6))
下标索引取出内容：num = t5[1][2]
index:查找某个元素的下标。num = t6.index(某个元素）
count:统计某个元素的数量。num = t6.count(某个元素）
len:计算某个元组的长度。num = len(t6)
元组遍历：while和for循环
while index < len(t8)
    print(f"元组元素有:{t8[index]}")
    index += 1

for element in t8:
    print(f"元组元素有:{element}")
元组数据不能修改的，会报错。如果在元组内部定义一个列表，那么元组中列表的数据可以修改。

字符串：str = "ithei python iop ituio"。不支持修改哦，和元组一样。
下标索引取值:从前往后或者从后往前。str[2]
查找某个字符的下标：str.index(字符或字符串)
替换字符，从而获得一个新字符串。new = str.replace(字符串1， 字符串2）
对字符串分割，会获得一个新列表：字符串.spilt(字符串，也就是你想以那个字符进行分割）
移除相应字符串：字符串.strip(移除空格或者指定字符)
统计字符串某个字符或者串出现的次数：字符串.count（字符串）
统计字符串长度:len(字符串)
字符串也有while和for循环遍历。
str1 = "qwert"
i = 0
while i < len(str1):
    print(str1[i])
    i += 1
    for i in str1:
    print(i)

数据容器的切片操作：下标是从0开始！！！
序列切片：会得到一个新序列。序列[起始下标：结束下标：步长],起始下标包括，但是结束下标不包括，所以一般结束下标会比想要的+1
起始下标可以留空，表示从头开始；结束下标可以留空，表示截取到结尾。
步长为1，一个个取元素；步长为N，每次跳过N-1个元素取。步长为负数，表示从后往前取。
切片倒序的话：[::-1]，记住啊，很好用

集合：不支持元素重复。（自带去重）
变量 = {元素， 元素，。。。},    空集合myset = set()
集合不支持下标索引访问，集合不是序列哦，但是和列表一样允许修改。
添加元素：set.add(待添加元素)
移除元素：set.removw(待移除元素)
随机取一个元素：element = set.pop(),随机取出一个元素放一个变量中
清空集合：set.clear()
取2个集合差集:set1.difference(set2),取出来集合1而集合2没有的元素构成一个新集合.
消除2个集合的差集：set1.defference_update(set2),在集合1内。删除和集合2相同的元素。注意！集合1会变化，集合2不变的。
集合合并：set1.union(set2),把set2放大set1后面，去重
统计集合元素数量：len(set),统计的是去重后的数量
集合遍历：不支持下标索引，所以不能用while循环。但是可以用for循环。

字典：存储的元素是一个个的键值对。不支持下标索引,不能用while循环
dict1 = {key:value, key:value, ..., key:value}
空字典，dict1 = {}或者dict2 = dict()
字典的key是不允许重复的,不可以使用下标索引，可以通过Key值来获取对应的value,new = dict1["树懒"]
字典可以嵌套，但是嵌套中key不能为字典，可以为其他的列表、元组、字符串等；value没有限制，可以是字典也可以是其他
嵌套字典：new = stu_dict["李杰"]["数学"]
字典的新增和更新:dict1["zhou"] = 99,zhou不存在的话就是新增，存在就是更改。
删除：score = dict.pop("zhou")
清空所有元素：dict1.clear()
获取全部的key：dict.keys()
遍历字典：通过上面获取到全部的key来完成遍历或者直接对字典进行for循环，每次循环直接得key。不能用while循环
统计字典里面的元素：len（dict1）

数据容器通用操作：都可以用for循环遍历
max：查找最大元素
min：查找最小元素
len：计算元素个数
list():转为列表
tuple():转为元组
str():转为字符串
set():装维集合
sorted(容器，[reverse = True])：正向排序。如果要倒序，就加上reverse = True

字符串比较：主要比较其对应的码值。ASCII码值，A = 65, a = 97.
按位比较，一位大整体就大

函数多返回值：用一个return后面接多个结果return 1， 2
然后调用时候x, y, z = return(),第一个变量接收第一个值，一一对应
函数传参的4种方式：
位置参数：一一对应传参，位置要对应齐
关键字传参：通过键=值，位置可以无序堆放。
位置参数与关键字参数混用时候，位置参数必须在前，多个位置参数还需要一一对应。
缺省参数：函数定义时候设置了默认参数，调用时候没有设置参数救用默认的。调用时候设置了参数，相当于修改了.
如果设置了默认值，必须在最后，不能在前面。
不定长参数：1位置参数不定长：参数用*args，数量不受限，都接收。所有参数会整合成一个元组。
          2关键字参数不定长：参数用**kwargs。数量不受限，但是要传入”键=值“形式，所有键值组成一个字典name = 'xiaowang'
函数作为参数传递：传入的是执行逻辑。把qwer的计算逻辑传入uio函数中。
def uio(qwer):
    result = qwer(1, 2)
    print(result)
def qwer(x, y):
    return x + y
uio(qwer)

lambda函数：定义匿名函数。只能写一行.uio(lambda x, y: x + y)
有名称的函数可以重复调用，匿名函数只能用一次。
函数体要写多行，还是def定义函数。

文件编码：主要用UTF-8编码操作。
文件读取操作：打开文件。open
文件两个read，后面read会接着前一个read的内容读取。
清华大学镜像：https://pypi.tuna.tsinghua.edu.cn/simple
ab173是一个json格式数据处理网站

类
定义：用class定义类。
class stu:   设计表格
    name = None
    gender = None
    age = None
qwe = stu()  打印表格
qwe.name = "lijie"   填写表格
qwe.gender = "man"
qwe.age = 20
print(qwe.name)
print(qwe.gender)
print(qwe.age)

类的具体定义和使用：属性（变量）、行为（类里面的函数）
方法：定义在类里面的函数。
class 类名称:
    成员变量
def 方法名（self，形参。。。。）
    方法体
对象 = 类名称（）

class stu:     通过self访问类内部成员变量。
    name = None

    def sayhi(self):
        print(f"大家好，我是{self.name}, 多多关照")

qwe = stu()
qwe.name = "周杰伦"
qwe.sayhi()


class stu:这里多了msg，也就是调用时候自己写是东西，是给msg的，会更丰富。
    name = None

    def sayhi(self):
        print(f"大家好，我是{self.name}, 多多关照")
    def sayhi1(self, msg):
        print(f"大家好，我是{self.name}, {msg}")

qwe = stu()
qwe.name = "周杰伦"
qwe.sayhi1("哎呦不错啊")

qwe1 = stu()
qwe1.name = "周杰"
qwe1.sayhi1("我很欣赏你")

面向对象编程：定义类之后，创建对象来完成具体工作。
class clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)
qwe = clock()
qwe.id = "1234560"
qwe.price = 20.2
print(f"闹钟的ID是{qwe.id}, 价格是{qwe.price}")
qwe.ring()

构造方法：__init__()
创建类对象时候，会自动执行，如果括号里面有数据，会自动传参给__init__方法使用。
class stu:
    name = None.如果这里不写的话，放到下面方法中也是可以的，就相当于先声明再赋值
    age = None
    tel = None
    def __init__(self, qwe, rty, uio):
        self.name = qwe。一定要记得调用赋值给类内部变量时候，要用self
        self.age = rty
        self.tel = uio
    print("stu类开始行动")
asd = stu("李杰", 24, "123456789")
print(asd.name)
print(asd.age)
print(asd.tel)

魔术方法：也就是python中的内置方法！！！
__init__构造方法
__str__字符串方法:
class stu:
    def __init__(self, qwe, rty):
        self.name = qwe
        self.age = rty
    # def __str__(self):
    #     return(f"{self.name}, {self.age}")
asd = stu("周杰伦", 32)
print(asd)
# print(str(asd))
如果没使用str方法，打印类对象是其内存地址，一般没啥用，用字符串方法，就会变成你的内容输出

__lt__()小于符号的比较方法
class stu:
    def __init__(self, qwe, rty):
        self.name = qwe
        self.age = rty
    def __lt__(self, uio):   不能直接用对象进行比较，要有lt构造方法进行比较。
        return self.age < uio.age

asd = stu("李杰", 36)
zxc = stu("拉拉", 68)
print(asd < zxc)
print(asd > zxc)

__le__()用于小于等于、大于等于两种比较运算符
class stu:
    def __init__(self, qwe, rty):
        self.name = qwe
        self.age = rty
    def __le__(self, uio):
        return self.age <= uio.age

asd = stu("李杰", 36)
zxc = stu("拉拉", 68)
print(asd <= zxc)
print(asd >= zxc)

__eq__()比较运算符实现方法，主要判断是否相等。
class stu:
    def __init__(self, qwe, rty):
        self.name = qwe
        self.age = rty
    def __eq__(self, uio):
        return self.age == uio.age

asd = stu("李杰", 32)
zxc = stu("拉拉", 36)
print(asd == zxc)

面向对象：基于模板（类）创建实体（对象），使用对象完成功能开发。
面向对象3大特性：封装、继承、多态。

封装：将现实事物封装到类中成员变量和成员方法。
私有成员变量：变量名开头加__。无法赋值，也无法获取数据。
私有成员方法：变量名开头加__。无法直接被类对象使用
class phone:
    __current_voltage = None

    def __keep(self):
        print("让CPU以单核模式运行")
qwe = phone()
print(qwe.__keep).运行不了，这是错误的。

私有成员无法被类对象使用，但是可以被类中其他成员使用。
class phone:
    __current_voltage = 2

    def __keep(self):
        print("让CPU以单核模式运行")
    def call(self):    call方法中访问了类内部的私有成员方法。
        if self.__current_voltage >= 1:
            print("5g通话已开始")
        else:
            self.__keep()
            print("单核开启")
qwe = phone()
qwe.call()

继承：一个类继承另外一个类的成员变量和成员方法。
单继承：class phone(uio)
多继承:class(uio, rty, qwe)
多继承中，如果父类有同名方法或者属性，先继承的优先权高于后继承的。
class Phone:
    IMEI = None
    producer = "HM"
    def call_by_4g(self):
        print("4g通话")
class Phone2022:
    face_id = "456132789"
    def call_by_5g(self):
        print("5g通话已经开启")
class NFC:
    nfctype = "第五代"
    producer = "HM"
    def read_card(self):
        print("NFC读卡")
    def writer_card(self):
        print("NFC写入")
class re:
    re_type = "红外遥控"
    def control(self):
        print("红外遥控开启了")

class Myphone(Phone, NFC, re):
    pass

phone = Myphone()
phone.call_by_4g()
phone.read_card()
phone.writer_card()
phone.control()

复写父类：子类继承父类成员变量和成员方法后。可以在自己类体在重新修改
class phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_back(self):
        print("使用5g通话")
class Myphone(phone):
    producer = "QWERT"
    def call_by_back(self):
        print("开启单核模式")
        print("使用5g通话")
asd = Myphone()
asd.call_by_back()
print(asd.producer)

调用父类：复写父类后，子类和父类就有一些相同的名字变量和方法。想调用以前父类的成员，如下
父类名.成员变量
父类名.成员方法（self）
class phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_back(self):
        print("使用5g通话")
class Myphone(phone):
    producer = "QWERT"
    def call_by_back(self):
        print("开启单核模式")
        print(f"父类厂商是{phone.producer}")
        phone.call_by_back(self)
        print("使用6g通话")
asd = Myphone()
asd.call_by_back()
print(asd.producer)

super().成员变量
super().成员方法（）
class phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_back(self):
        print("使用5g通话")
class Myphone(phone):
    producer = "QWERT"
    def call_by_back(self):
        print("开启单核模式")
        print(f"父类厂商是{super().producer}")
        super().call_by_back()   这里害不需要写self，很方便。
        print("使用6g通话")
asd = Myphone()
asd.call_by_back()
print(asd.producer)

类型注解:变量：函数（方法）形参和返回值
变量注解：变量：注解    var1: int = 10  定义的变量名：类型=给变量赋的值
类对象注解：class student
              pass
          stu: student = student()
容器注解：简易mylist: list = [1, 2, 3]
详细   mylist: list[int] = [1, 2, 3]
元组需要对每一个元素进行标记：mytuple = tuple[str, int, bool] = ("yui", 666, False)
字典需要对键和值都要注解:mydict: dict[str, int] = {"yui": 444}
也可以在注释中进行注解：#type: int
var_1 = random.randint(1, 10)     #type: int(这里值得是变量var_1的类型)
为变量设置注解，显示的变量定义，一般不需要注解。var1： int = 10
一般在无法直接看出变量类型的时候，再回添加变量的类型注解

函数（方法）的类型注解-形参注解.def 函数（方法）名（形参名:类型, 形参名：类型。。。。）
def add(x: int, y: int):
return x + y
函数（方法）的返回值也可以添加类型注解
def 函数（方法）名(形参： 类型， 形参： 类型。。。。。。） -> 返回值类型:
    pass

Union联合类型注解：导包 from typing import union
Union[类型， 类型。。。].可以在字典、变量注解、函数（方法）形参和返回值注解中均可以使用
from typing import Union

mylist: list[Union[int, str]] = [1, 2, "fgyt", "sddff"]

def func(data: Union[int, str]) ->Union[int, str]:
    pass
func()

多态：使用不同对象会有不同状态
class Animal:
    def speak(self):
        pass   这里就是抽象类，空实现，定义一个标准，让子类来具体实现方法
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
def makenoise(animal: Animal):
    animal.speak()
dog = Dog()
cat = Cat()
makenoise(dog)
makenoise(cat)

class AC:   父类做顶层设计，定义一些抽象方法，子类具体来实现。
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing(self):
        pass
class Midea(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing(self):
        print("美的空调摆风")
class Geli(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing(self):
        print("格力空调摆风")

def makecool(ac: AC):
    ac.cool_wind()

midea = Midea()
gree = Geli()
makecool(midea)
makecool(gree)
定义函数（方法）， 通过类型注解声明需要父类对象， 实际传入子类对象进行工作，获得不同工作状态。
没有具体实现的方法称之为抽象方法（pass）
抽象类一般做顶层设计，以便于子类做具体实现，要求子类必须复写父类一些方法。
"""




