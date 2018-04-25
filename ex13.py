#coding=utf-8
#sys是模组（库）
from sys import argv
#argv[0]即当前程序名，这是模块的固有定义，此处只是调用了这一个功能。故实际只有3个参数
#“import”可以作为提示，让他们明白你的代码用到了哪些功能。
#argv 是所谓的“参数变量(argument variable)”


#参数解包，依次赋予左边的参数名
script,first,second,third = argv

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)

