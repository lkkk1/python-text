#coding=utf-8
#字符串包含字符串  标记*

x = "There are %d types of people." % 10
#二进制
binary = "binary"
do_not = "don't"
# *(字符串包含字符串)
y = "Those who know %s and those who %s." %(binary,do_not)

print(x)
print(y)

#  %r  直接显示 不需要再加‘’
# *
print("I said: %r" % x)
#  %s  智能处理掉了‘’，需要再单独加。
# *
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#格式化字符在输出函数中才用。
# *
print(joke_evaluation  % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
