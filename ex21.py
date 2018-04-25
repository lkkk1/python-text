# coding = utf-8
def add(a,b):
    print("ADDING %d + %d"%(a,b))
    return a+b

#return 返回一个值，在调用函数时，直接将该返回值赋给变量
def subtract(a,b):
    print("SUBTRACTING %d - %d"%(a,b))
    return a-b

def multiply(a,b):
    print("MULTIPLYING %d * %d"%(a,b))
    return a*b

def divide(a,b):
    print("DEVIDING %d / %d"%(a,b))
    return a/b

print("Let's do some math with just functions!")

#C中的左值右值，左值即地址，右值即该返回数值
age = add(20,3)
height = subtract(79,3)
weight = multiply(88,2)
iq = divide(480,2)

print("Age:%d,Height:%d,Weight:%d,IQ:%d"%(age,weight,height,iq))

#A puzzle for the extra credit,type it in anyway.

print("Here is a puzzle.")

t1=divide(iq,2)
t2=multiply(weight,t1)
t3=subtract(height,t2)
what=add(t3,age)
#what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes:",what,"Can you do it by hand?")