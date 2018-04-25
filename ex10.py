# coding = utf-8
#\t 表示跳转到下一个横向制表符
tabby_cat = "\t I'm tabbed in."

persian_cat = "I'm split\n on a line"
backslash_cat = "I'm \\ a \\ cat."


#\v 表示跳转到下一纵向制表符

#'''和"""作用一样 都是打印内部所有内容。  ！注释都不行
fat_cat = '''
I'll do a list:
#注释都不行
\v* Cat food 
\v* Fishies
\t* Catnip \n\t* Grass
'''

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

#定义字符串变量 记得加引号！
M="Mr.Liang"
Q="Hi \n\v %s \n%r"
#在字符串引号中再次使用引号，用引号转义符。
#%r  全部打印  %s 智能选择了我想表达的。
print("hello \n\vTian,\n\v%s"% tabby_cat)
Y="Welcome to \'Tian\'."
print(Q % (M,Y))