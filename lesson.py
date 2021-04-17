import random

print("you in dark room misty castle.")
print("you have 3 door.plase choose one.")
playerChoice = input("choose1,2,3 or 4...")
if playerChoice == "1":
    print("you find room with   golden.you a rich man!")
    print("you win!")
elif playerChoice == "2":
    print("door open and angry trol hit you he's weapon.")
    print("sorry, but you game over.")
elif playerChoice == "3":
    print("you went to room and find a slippy dragon.")
    print("you can do:")
    print("1) roberry dragon golden")
    print("2) walk to sun")
    dragonChoice = input("chose 1 or 2")
    if dragonChoice == "1":
        print("sorry,but dragon get up and eat you and you yummy.")
        print("sorry,but you game over.")

    elif dragonChoice == "2":
        print("you run  of  misty  castel")
        print("you win!")
    else:
        print("sorry but you don't write 1 or 2!")

elif playerChoice == "4":
    print("you went to room with cat")
    print("you should says number(1,10) that he expect")
    number = int(input("your number is..."))
    cat_number = random.randint(1, 10)
    if number == cat_number:
        print("cat says: it's true number")
        print("you are free")
        print("you win!")
    else:
        print("cat says:it's don't true number, my number is: %s" % cat_number)
        print("fro now you don'tsee sun")
        print("sorry,but you game over")
else:
    print("sorry,but you don't write 1,2,3 or  4")
    print("restart game and play")
