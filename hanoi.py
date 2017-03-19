# 【 ハノイの塔 】
# 〜　ヒント　〜
# 3本の杭A,B,Cがある。最初Aに円盤が、大きいものが下になるように積まれている。
# 円盤を順序を大きいものが下になるように常に保ちつつ、AからCに移動する。
# 全ての円盤がn個の時、
# (1) 上から n - 1 個目までの円盤を「何らかの方法」でAからBに移動する。
# (2) 残った1枚をAからCに移動する。
# (3) Bにある円盤を「何らかの方法」でBからCに移動する。
#  | ここで、(1)は最初Aに n - 1 個の円盤があり、Bにすべての円盤を移動させるという問題ととらえることができる。
#  | そこで、次のようにする。
# (1) 上から n - 2 個目までの円盤を「何らかの方法」でAからCに移動する。
# (2) 残った1枚をAからBに移動する。
# (3) Cにある円盤を「何らかの方法」でCからBに移動する。
#  | (3)も同様にして行うことができ、『何らかの方法』の部分を分解していくと解ける。
# 参照元：https://ja.wikipedia.org/wiki/ハノイの塔

# リストの右側を杭の上側に見立てること。
# より大きい数字をより大きい円盤に見立てること。
m_stick_A = list(range(5,0,-1))
m_stick_B = []
m_stick_C = []

def move_X_to_Y(list_X, list_Y):
    try:
        list_Y.append(list_X[-1])
        del list_X[-1]
    except:
        print("error")
    finally:
        return

counter = 0                                              # 手順数を数える
def hanoi(start_p, pass_p, end_p, n):
    if n-1 > 0: hanoi(start_p,end_p,pass_p,n-1)
    # print("\n",m_stick_A,m_stick_B,m_stick_C,sep="\n") # 過程を表示する
    move_X_to_Y(start_p,end_p)
    global counter                                       # 手順数を数える
    counter += 1                                         # 手順数を数える
    if n-1 > 0: hanoi(pass_p,start_p,end_p,n-1)

hanoi( m_stick_A, m_stick_B, m_stick_C, len(m_stick_A) )
print("\nfinal.",m_stick_A,m_stick_B,m_stick_C,sep="\n") # 最終結果を表示する
print("手順数:2^n - 1 =",counter)                         # 手順数を数える
