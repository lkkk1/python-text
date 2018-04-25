#coding=utf-8
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print("You have %d cheeses!"%cheese_count)
    print("You have %d boxes of cracters!"%boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
#调用函数并带入两个参数
cheese_and_crackers(20,30)


#varibles  变量
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#调用定义的两个变量作为函数参数
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too:")
#引入的实参是一个运算式
cheese_and_crackers(10+20,5+6)

print("And we can combine the two,variables and math:")
#引入的实参一个变量运算
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)