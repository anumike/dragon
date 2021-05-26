import random
number = random .randint(1, 20)
guess = int(input("I random number(1,20)My number is..."))
while guess != number:
    if guess < number:
        print("your number small...")
    else:
         print("your number big...")
    guess = int(input("plese,try agin..."))
print("it's true number! you win!")