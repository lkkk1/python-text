people = 25
cars = int(input(" num cars:"))

if people > cars:
    print("Too much people!")
#elif 等同于 else if ,
# 就是上一个 if 不成立就到这里判断这个 if ； else 就是之前的 if 不成立，就运行这个。
elif people < cars:
    print("Too much cars!")
#不管elif还是else  最后都有：
else:
    print("Equal!")