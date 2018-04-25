from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    next_choose = input(">>>")
    if "0" in next_choose or "1" in next_choose:
        how_much = int(next_choose)
    else:
        dead("Man,learn to type a number:")


    if how_much < 50:
        #greedy 贪心
        print("Nice, you are not greedy.You win!")
        #在很多类型的操作系统里，exit(0) 可以中断某个程序，
        #exit(1) 表示发生了错误，而 exit(0) 则表示程序是正常退出的。
        exit(0)
    else:
        #贪婪的混蛋
        print("You greedy bastard!")

def bear_room():
    print("There is a bear there.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next_choose = input(">>>")

        if next_choose == "take honey":
            #熊看着你，然后打你的脸。
            dead("The bear looks at you then slaps your face off.")
        #taunt bear    嘲弄熊
        elif next_choose == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.You can go through it now.")
            bear_moved = True
        elif next_choose == "taunt bear" and bear_moved:
            #get pissed of  生气
            dead("The bear gets pissed off and chews your leg off.")
        elif next_choose == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    #在这里，你看到邪恶的邪神克苏鲁。
    print("Here you see the great evil Cthulhu.")
    #他一直盯着你，你就疯了
    print("He, it， whatever stares at you and you go insane.")
    #你是要逃命还是让我吃掉你的头
    print("Do you flee for your life or eat your head?")

    next_choose = input(">>>")

    if "flee" in next_choose:
        start()
    elif "head" in next_choose:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next_choose = input(">>>")

    if next_choose == "left":
        bear_room()
    elif next_choose == "right":
        cthulhu_room()
    else:
        #你在房间里徘徊直到你饿死。
        dead("You stumble around the room until you starve.")

start()

# TODO HAHHA


