#coding = utf-8
#在定义函数时，应注意除了函数内新定义的变量，其他在函数中用到的变量，
#都应该放在函数目录下。否则就会报错

def While(n,m):
    i = 0
    numbers = []

    while i < n:
        print("At the top i is %d" % i)
        numbers.append(i)
        i += m
        print("Numbers now:", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers:")

    for num in numbers:
        print(num)

#注意用户输入的是字符串类型，要转为int类型才能比较。
n = int(input("最大的范围值是？\n>>>"))
m = int(input("i的递增加值是？\n>>>"))
While(n,m)
