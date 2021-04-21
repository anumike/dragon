aliens = 2
password = "ALIENS"
print("faster! aliens attack we!")
print("you  the global defense system needs to be activated")
print("I hope, you can write password  which will save the earth...")
print()
print("-------------------------------------------------------------")
print("     welcomes global defense network       ")
print("--------------------------------------------------------------")
print()
guess = input("plase write password: ").upper()
while guess != password:
    print()
    print("password wrong")
    print()
    aliens = aliens ** 2
    print("Now",aliens, "aliens on our planet.Try again !")
    if aliens > 7400000000:
        break

    print()
    print("password hint: these are the ones who attack us")
    print()
    guess = input("faster!plase write password:").upper()
if aliens >74000000000:



    print("of n-o-o!We ost the battle.")

else:
    print("hooray! we win the  battle!")
