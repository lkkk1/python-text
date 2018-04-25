#coding=utf-8
from sys import argv

script,input_file=argv

def print_all(f):
    print (f.read())

#rewind  倒带
def rewind(f):
#seek()方法用于移动文件读取指针到指定位置。
# 默认0表示从文件头开始读，1表示从当前位置开始读，2表示从文件尾开始读。
    f.seek(0)

def print_a_line(line_count,f):
#打印 行号，对应行
    print(line_count,f.readline())

#此处将open和前边的f.read()功能分割了。
#避免了两个函数写两次open.
#但还是先open再.read(),总体流程是不变的。

current_file = open(input_file,'r')

print("First let's print the whole file:\n")

#打印全文
print_all(current_file)

print("Now let's rewind,kind of like a tape.")

#打印指针重新指向文章开头
rewind(current_file)

print("Let's print three lines:")


current_file.close()
current_file = open(input_file,'rb+')
#打印第一行
current_line = 1
print_a_line(current_line,current_file)


#readline()在没有rewind指针重新定位的情况下会按顺序自动往下读。
current_line = current_line+1
current_file.seek(2,1)
print_a_line(current_line,current_file)

current_line = current_line+1
print_a_line(current_line,current_file)



#  += 就是先+再=
a=3
b=6
#   即  a = a+b
a+=b
print(a)