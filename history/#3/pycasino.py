from random import randint

from numpy import tri

print("Welcome to pycasino!")
pc_choice = randint(1,100)

playing=True
tried=0

while playing:
    user_choice = int(input("choose your number(1~100) :"))
    if user_choice==pc_choice:
        playing=False
        print("You Won!")
        print("you tried :",tried)
    elif user_choice > pc_choice:
        tried+=1
        print("lower!")
    elif user_choice < pc_choice:
        tried+=1
        print("higher!")