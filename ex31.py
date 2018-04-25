print("You enter a dark room with two doors. ",end='')
print("Do you go through door #1 or door #2?")
print("Door #3 Python")

door = input(">>>")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1.Take the cake.")
    print("2.Scream at the bear.")

    bear = input(">>>")

    if bear == "1":
        print("Thr bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well,doing %s is probably better.Bear runs away."%bear)

elif door == "2":
    print ("You stare into the endless abyss at Cthulhu's retina")
    print("1.Blueberries.")
    print("2.Yellow jacket clothespins.")
    print("3.Understanding revolvers yelling melodies.")

    insanity = input(">>>")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

elif door == "3":
    print("选择Python的理由")
    print("1.入门编程，进阶开发")
    print("2.人生苦短，我用Python")

    choose = input(">>>")
    if choose == "1" or choose == "2":
        print("加油，路漫漫其修远兮。")
    else:
        print("别乱选！ 看不懂中文吗，你挂了！")


else:
    print("You stumble around and fall on a knife and die. Good job!")