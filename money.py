print('you have money ...')


def money():
    if int(ask()) >1000:
        print('i rich!')
    else:
        print("i don't rich!!")
        print('But someday I can and will ...')


def ask():
    return input("how many ?")


money()

