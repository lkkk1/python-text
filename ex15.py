#coding = utf-8
from sys import argv

script,filename = argv

#用命令行参数获取文件名
'''
open和你自己的脚本、或者 raw_input 命令类似，它会接受一个
参数，并且返回一个值，你可以将这个值赋予一个变量。这就是你打开文件的过
程。
'''
txt = open(filename)

print("Here's your file %r:"%filename)
'''从 open 获得的东西是一个 file (文件)，文件本身也支持
一些命令。它接受命令的方式是使用句点 .紧跟着你的命令，
'''
print(txt.read())


#用input获取文件名
#print("Type another filename:")
file_again = input("Type another filename: \n>>>")

txt_again = open(file_again)

print(txt_again.read())