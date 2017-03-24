# # モジュール
# # プログラムが大きくなると、複数のファイルに分けたくなるだろう。
# # その時に役に立つのがモジュール(module)という機能。
# # Pythonではスクリプトが書かれた一つのファイルを「一つのモジュール」として扱うことができる。
# # モジュールの中で定義した関数などを、他のファイルの中で利用できる。
# # モジュールを読み込む命令がimport。
# # 書式：
# import モジュール名

# import my_module
# print(my_module.inch_to_cm(30))
# 長い。どうすればいい？ー＞2つ方法
# in_to_cm = my_module.inch_to_cm
# print(in_to_cm(90))
# from my_module import inch_to_cm
# print(inch_to_cm(30))
# # 書式：
# from モジュール名 import 要素1, 要素2, ...
# from my_module import * #モジュール内のすべての要素を取り込む

# # 異なるパスにモジュールを設置した時は。
# import mod.my_module #mod/my_module.pyをインポート
# #####import "/Users/qiushi/workspace/Python/my_module"


# # 練習
# # サイコロを作ろう
# import random
# r = random.randint(1,6)
# print(r)

import datetime
datetime.date.today()
