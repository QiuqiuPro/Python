# Hanoi part 1 - Question

m_list_a = list(range(20))
m_list_b = []

# 関数moveを定義する
# 引数はlist_a, list_b, nとする
# 関数の機能は、次の通り：
#     条件判断をして、もし(n <= 0)なら関数を終了する。
#     list_aの第n-1項目をlist_bに追加する(append)
#     その項目を消去する(del)
#     関数自身を再帰的に呼び出す。ただしn-1とする。

# [ここにプログラムを書いてください]

move( m_list_a, m_list_b, len(m_list_a) )
print(m_list_a, m_list_b, sep='\n')
# 結果が次の通りなら成功：
# []
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
