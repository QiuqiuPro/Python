from random import randint

dice = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0
}
for i in range(10000):
    dice[randint(1,6)] += 1

print(dice)
