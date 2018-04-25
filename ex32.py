the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
#mixed list
change = [1,'pennies',2,'dimes',3,'quarters']

for number in the_count:
    print("This is count %d "% number)

for fruit in fruits:
    print("A fruit of type:%s"%fruit)

# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r"% i)

#build list

#elements = list(range(0,6))
#print(elements)
#then use the range function to do 0 to 5 counts


#python3中 range() 函数可返回一个迭代值，看似列表而不是列表，
# 一般用在 for 循环中。
elements = []
#将0-6范围内的每个数字依次装入变量i中，执行下列操作。
for i in range(0,6):
    print("Adding %d to the list."%i)
    #append is a function that list understand
    #append() 方法用于在列表末尾添加新的对象，写入内容
    #此处append函数才是真正把迭代值放入列表的关键，类似于上边的list()
    elements.append(i)


#now we can print them out too
for i in elements:
    print("Elements was : %d"% i)


#range()可以动态创建一组list，将字符串'runaway'以单个字母分割，分别存入列表中。
x='runaway'

for i in list(range(len(x))):
    print(x[i])