from random import randint

user_choice = int(input("choose your number(1~100) : "))
pc_choice = randint(1,100)

if user_choice == pc_choice:
    win=True
    print("You Win")
elif user_choice > pc_choice:
    print("Lower! Computer choose",pc_choice)
elif user_choice < pc_choice:
    print("Higher! Computer choose",pc_choice)