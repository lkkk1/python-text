#coding=utf-8
def choose(ans1,ans2):
    print("do your choose:")
    print("IF Ti ,call %d"%ans1)
    print("If uestc,call %d"%ans2)

print("case1:")
choose(1,2)

print("case2:")
a=1
b=2
choose(a,b)

print("case3:")
a=1
choose(a,2)

print("case4:")
a=1
choose(a+5,8)

print("case5:")
a=int(input("GET the first num:\n>>>"))
b=int(input("GET the second num:\n>>>"))
choose(a,b)