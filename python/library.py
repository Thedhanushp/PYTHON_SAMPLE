import random
from random import choice
# random.choice
coin = random.choice(["heads","tails"])
print(coin)

# random.randint
number = random.randint(1,10)
print(number)

#random.shuffle
cards = ["jack","queen","king"]
random.shuffle(cards)
for i in cards:
    print(i)