#coding=utf-8
print('I will now count my chickens:')

print('Hens',25+30/6)  #python3中为真除法（无论任何类型都会保持小数部分，即使整除也会表示为浮点数形式）。
print('Roosters',end=' ')  #end=''连接两个不同的print语句输出
print(100-25*3%4)
print('Now i will count the eggs:')
print(3+2+1-5+4%2-1/4+6)
print('Is it true that 3+2<5-7?')
print(3+2<5-7)

print('What is 3+2?',3+2.0)
print("What is 5-7?",5-7)

print("Oh,that's why it's False.")  #python3中 双引号单引号同时用到时应避免都用单引号或者都用双引号，避免歧义。
print('How about some more.')
print('Is it greater?',5>-2)
print('Is it greater or equal?',5>=-2)
print('Is it less or equal?',5<=-2)
#python3除法默认浮点运算
#python2除法默认整数运算，要浮点运算必须写成浮点型 如2.0
'''
%是个运算符。对于整数，是取余运算。    对于字符串，是c风格的字符串格式化运算。
n = "Aki"
"My name is %s" % n
'''
