#coding = utf-8
from sys import argv

script,user_name,ans = argv
#prompt  提示
prompt = '>>>'

print("Hi %s,I'm the %s script."%(user_name,script))
print("I'd like to ask you a few questions.")
print("Do you like me %s"% user_name)
likes = input(prompt)

print("Where do you live %s?"% user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
print("""
Alright, so you said %r about linking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
"""%(likes,lives,computer))

print("Who's your love?")
ques = input(prompt)
print("""
Are you sure your answer is this?
I love %s
And you? %s
"""% (ans,ques))



#熟悉input()的使用，区分input()和argv命令行参数，一个在程序开始要求输入，一个在程序中交互时输入

