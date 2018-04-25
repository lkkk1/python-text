def For_achieve(n):
    numbers = []
    for i in range(0,n):
        #for循环的遍历，刚好是从第一个到最后一个。
        print("At the top i is %d"%i)
        numbers.append(i)
        print("Numbers now:", numbers)
        #此时i+=2的设置已经没有意义。
        # 因为for的遍历性，会从头到尾每个都执行，故相当于已经默认i+=1。再设置i+=2也不会影响整体的执行。
        #i = i + 2
        #print("At the bottom i is %d" % i)

    print("The numbers:")

    for num in numbers:
        print(num)

For_achieve(3)
