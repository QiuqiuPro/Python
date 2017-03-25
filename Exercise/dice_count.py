from random import randint

dice = { i:0 for i in range(1,7) }
print(dice)
for i in range(60000):
    dice[randint(1,6)] += 1
print(dice)
