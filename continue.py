import random

while True:
    WOMAN = ["SCIENTIST", "queen,", "pirate,", "giant rabbit."]
    MAN = ["POLICE OFFICER", "artist", "grendfather,", "robo-killer"]
    place = ["on planet", "in supermarket", "in caves"]
    sheWore = ["suit for scuba diving", "butterfly wings", "paper bag"]
    heWore = ["purple suit", "shark costume", "beach towel"]
    womanSays = ["'Who are you?'", "you understand what case ?'", "'why?'"]
    manSays = ['"beep-boop'"", 'not eat frogs!', "what time is it?"]
    consequence = ["world peace.", "chaos.", "giant leg crushed everyone.", "rainbows."]
    worldSaid = ["'bizarre nonsense!'", "cheese is now in vogue", "I'm melting!"]
    print(random.choice(WOMAN), "met", random.choice(MAN), random.choice(place))
    print("sheWore in", random.choice(sheWore))
    print("heWore",random.choice (heWore))
    print("manSays", random.choice(manSays))
    print("womanSays",random.choice (womanSays))
    print("consequence became", random.choice (consequence))
    print("world said",random.choice (worldSaid))
    print()
    input("press <Enter> and restart game")
    print()
