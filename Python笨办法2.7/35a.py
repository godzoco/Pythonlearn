#coding=utf-8
from sys import exit

#引入exit 功能 即使 exit（0）正常退出 exit（1） 异常退出

def gold_room():
    '''
    这个定义一个 黄金房子  在里面输入数字
    @但是next = raw_input("> ") 他这句没有 转化  直接输入的 33 1 0
    这些 都是字符串     只有 "0" 和  "1" 他写了 转化
    
    #最多拿就是41
    > 41
Nice, you're not greedy, you win!
    '''
    #所以 输入 其他 33  22 这些 都变成了 字符串  没有用 int(next)识别 装化到how_much
    #所以只要有输入 0或者是 1 就可以  但是过50不行
    #告知输入问题  要你学会输入数字 或者是 你贪婪死  
   # > 111110000
#You greedy bastard! Good job!
#输入 111110000 就贪婪死
    print "This room is full of gold.  How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

#在熊的房间  必须 先 taunt bear  嘲讽 熊离开打开的门
# 然后 离开之后  开始 进去 然后
'''
@bear_moved = True
'''
# 第一次 嘲讽之后 熊激怒了  行动 的变量 开启
#再taunt bear  就死了 这时候open door 开启门 逃走
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then pimp slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your crotch off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

# 在这个深渊房 必须输入 逃走flee
#再才能start（）重新开始

def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()

#打印每次死的 原因
def dead(why):
    print why, "Good job!"
    exit(0)
#加人最开始的部分
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
 
#left taunt bear open door 41  是解题答案
