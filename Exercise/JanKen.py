from random import randint
l_te = ["Gu", "Choki", "Pa"]

while True:
    player_te = input("Jan-Ken-Pon!\n(input Gu or Choki or Pa)\n>")
    if player_te in l_te:
        break
    else:
        print("Error: Gu Choki Pa only please.")
        continue

pc_te = l_te[randint(0,2)]

def jankenWinner(te_a, te_b):
    if (te_a == "Gu" and te_b == "Choki") or (te_a == "Choki" and te_b == "Pa") or (te_a == "Pa" and te_b == "Gu"):
        return "pc"
    elif te_a == te_b:
        return None
    else:
        return "player"

result = jankenWinner(pc_te, player_te)
if result != None:
    print("PC:{0}\nPlayer:{1}\n{2} wins!".format(pc_te, player_te, result))
else:
    print("Both {0}. Draw".format(pc_te, player_te, result))
