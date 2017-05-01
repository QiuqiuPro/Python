from matplotlib import pyplot as plt
# # 3.1
# # pyplot
# # 折れ線グラフ pyplot.plot()
#
# years = list(range(1950, 2011, 10))
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
# # 折れ線グラフを作る。X軸を年、Y軸をGDPとする。
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# # タイトルを追加
# plt.title('Normal GDP')
# # Y軸にラベルを追加
# plt.ylabel('Billions of $')
# plt.show()


# 3.2
# # 棒グラフ pyplot.bar()
# movies = ['Annie Hall', 'Ben-Hur', 'Casablanca', 'Gandhi', 'West Side Story']
# num_oscars = [5,11,3,8,10]
#
# # xs = [i + 0.1 for i, _ in enumerate(movies)]
# xs = list(range(len(movies)))
# # 昔はX軸の座標を考慮してリストを調整する必要があったようだが、おそらくアップデートで自動調整してくれるようになったらしい。
#
# plt.bar(xs, num_oscars)
#
# plt.ylabel('# of Academy Awards')
# plt.title('Epic Movies')
#
# # plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
# plt.xticks(list(range(len(movies))), movies)
#
# plt.show()

# # 棒グラフでヒストグラム
# grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
# decile = lambda grade: grade // 10 * 10 # decile:（統計）デシル。10分位数。
# # Counterクラスで、あるデシルの出現頻度をカウントする。
# from collections import Counter
# histogram = Counter(decile(grade) for grade in grades)
#
# plt.bar([x for x in histogram.keys()], # またはlist(histogram.keys())
#         histogram.values(),
#         8)
#
# plt.axis([-5,105, 0,5]) # 表示範囲を指定。X軸は-5から105、Y軸は0から5まで。
#
# plt.xticks([10*i for i in range(11)])
# plt.xlabel('Decile')
# plt.ylabel('# of Students')
# plt.title('Distribution of Exam 1 Grades')
# plt.show()


# # 3.3
# # 折れ線グラフ
# variance = [1,2,4,8,16,32,64,128,256]
# bias_squared = [256,128,64,32,16,8,4,2,1]
# total_error = [x+y for x,y in zip(variance, bias_squared)]
# xs = [i for i, _ in enumerate(variance)]
#
# # pyplot.plot()を複数回呼び出して、一つのグラフに複数の線を描画可能。
# plt.plot(xs, variance, 'g-', label='variance')
# plt.plot(xs, bias_squared, 'r-', label='bias^2')
# plt.plot(xs, total_error, 'b:', label='total error')
#
# plt.legend(loc=9) # loc=9 => 上部中央
# plt.xlabel('model complexity')
# plt.title('The Bias-Variance Tradeoff')
# plt.show()


# 3.4
# 散布図
friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(   label,
                    xy=(friend_count, minute_count),
                    xytext=(5, -5),
                    textcoords='offset points')

plt.title('Daily Minutes vs Number of Friends')
# plt.axis('equal') # 軸を比較したい場合、軸の長さを同じに指定する
plt.show()
