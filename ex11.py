#coding = utf-8
#新的print会默认换行，要让用户的输入跟在问题后，需要用到一个end=""
print("How old are you?",end = "")
age = input()
print("How tall are you?",end = "")
height = input()
print ("How much do you weight?",end = "")
weight = input()


print("So,you're %r old,%r tall and %r heavy."%(age,height,weight))

'''
#Text
print ("为什么选择考研？", end="")
ans=input()
print("为什么选择python?", end="")
ans1=input()
print ("请输入 必有回响", end="")
W=input()
print("念念不忘，%s"%W)
'''