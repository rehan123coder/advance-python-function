import random
import time
number=random.randint(1,100)
def intro ():
    print(" may I ask your name")
    global name
    name = input()
    print( "hi" ,name, "i am going to selecet a number from 1 to 100 and you have to guess the number by thinking ")
    if number %2==0:
        x='even'
    else:
        x='odd'
    print("this is an x number")
    time.sleep(0.5)
    print("go ahed and guess the number")
def pick():
    guesstaken=
