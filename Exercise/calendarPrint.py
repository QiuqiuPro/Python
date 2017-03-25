week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
def getMonth(year):
    month = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    if (year%4==0) and (year%100!=0) or (year%400==0):
        month['Feb']=29
    return month

# 2000/1/1 is Sat.

#"Day Of The Week" dotw
#知りたい曜日を計算する
# 引数：知っている日の曜日、知りたい日のその日からの経過日数
# 戻り値：曜日
def calcDotw(known_dotw,days_between):
    i_dotw = week.index(known_dotw)
    unknown_dotw = i_dotw + days_between
    return week[unknown_dotw%7]

#calcDotw("Tue",30)

# ある年からある年までの、「日数」を計算する
# 引数：曜日が既知である年（k）と、曜日を知りたい年（u）
# 戻り値：k年からu年の直前までの、日数の総和
# calcDaysBtwnYears(2000,2017)
def calcDaysBtwnYears(known_y,unknown_y):
    show_year_in_days = lambda x: ( (x*365) + (x//4) - (x//100) + (x//400) ) # unit conversion: year->days
    return show_year_in_days(unknown_y -1) - show_year_in_days(known_y -1)

# ある月のカレンダーを表示する
# 引数：月の名前、最初の日のようび、何日あるのか
# 戻り値：なし
# 機能：テキストファイルに書き出す
def printMonth(month,dotw,days):
    '''例: printMonth("Jan","Tue",30[,print_func=someFunc])'''
    with open("/Users/qiushi/workspace/Python/Exercise/cal/"+month+".txt","w") \
    as f:
        f.write(month.center(28)+"\n")
        for y in week:
            f.write( y+" " )
        f.write("\n")
        # suppose dotw="Tue" => t==1
        t = week.index(dotw)
        f.write( "    "*t )
        for i in range(1,days+1):
            f.write( " "+str(i).rjust(2)+" " )
            if (t+i)%7 == 0:
                f.write("\n")
        f.write( "    "*(7-(t+days)%7) )

# 一年のカレンダーを表示する
# 引数：年
# 戻り値なし
# 機能：表示
def writeCalYear(year):
    dotw = calcDotw("Sat",calcDaysBtwnYears(2000,year))
    for month, day_num in getMonth(year).items():
        printMonth(month,dotw,day_num)
        dotw = calcDotw(dotw,day_num)

writeCalYear(2017)

# カレンダーを表示する
# 引数：表示レイアウトを示すタプル
# 戻り値なし
# 機能：表示
def showCal(tpl):
    '''例： showCal( (3,4) )'''
    
