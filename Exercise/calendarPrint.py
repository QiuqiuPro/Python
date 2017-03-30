week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
week = ["Wed","Thu","Fri","Sat","Sun","Mon","Tue"]
def getMonth(year):
    month = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May':31, 'Jun':30, 'Jul':31, 'Aug':31, 'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
    if (year%4==0) and (year%100!=0) or (year%400==0):
        month['Feb']=29
    return month

# 2000/1/1 is Sat.
#"Day Of The Week" -> dotw

#知りたい曜日を計算する
# 引数：知っている日の曜日、知りたい日のその日からの経過日数
# 戻り値：曜日
def calcDotw(known_dotw,days_between):
    '''例: calcDotw("Tue",30)'''
    i_dotw = week.index(known_dotw)
    unknown_dotw = i_dotw + days_between
    return week[unknown_dotw%7]

# ある年からある年までの、「日数」を計算する
# 引数：曜日が既知である年（k）と、曜日を知りたい年（u）
# 戻り値：k年からu年の直前までの、日数の総和
def calcDaysBtwnYears(known_y,unknown_y):
    '''例: calcDaysBtwnYears(2000,2017)'''
    show_year_in_days = lambda x: ( (x*365) + (x//4) - (x//100) + (x//400) ) # unit conversion: year->days
    return show_year_in_days(unknown_y -1) - show_year_in_days(known_y -1)

# ある月のカレンダーを表示する
# 引数：月の名前、最初の日のようび、何日あるのか
# 戻り値：なし
# 機能：テキストファイルに書き出す
# def printMonth(month,days,dotw):
#     '''例: printMonth("Jan",30,"Tue")'''
#     with open("/Users/qiushi/workspace/Python/Exercise/cal/"+month+".txt","w") \
#     as f:
#         f.write(month.center(28)+"\n")
#         for y in week:
#             f.write( y+" " )
#         f.write("\n")
#         # suppose dotw="Tue" => t==1
#         t = week.index(dotw)
#         f.write( "    "*t )
#         for i in range(1,days+1):
#             f.write( " "+str(i).rjust(2)+" " )
#             if (t+i)%7 == 0:
#                 f.write("\n")
#         f.write( "    "*(7-(t+days)%7) )

# ある月のカレンダーを辞書型にする
# 引数：ある年のカレンダーの辞書型、月の名前、何日あるのか、最初の日のようび
# 戻り値：なし
# 機能：year_dicに月の要素(list)を追加する
def storeCalMonth(year_dic,month,days,dotw):
    '''例: storeCalMonth({},"Jan",30,"Tue")'''
    cal_lst=[]
    cal_lst.append(month.center(28)) #"{0:^28}".format(month)
    s=""
    for d in week:
        s += d+" "
    cal_lst.append(s)
    s=""
    # suppose dotw="Tue" => t==1
    t = week.index(dotw)
    s += "    "*t
    for i in range(1,days+1):
        s += " "+str(i).rjust(2)+" "
        if (t+i)%7 == 0:
            cal_lst.append(s)
            s=""
    else:
        s += "    "*(7-(t+days)%7)
        cal_lst.append(s)
        s=""
    if len(cal_lst) < 8:
        for i in range(8-len(cal_lst)): cal_lst.append("".center(28))
    year_dic[month]=cal_lst

# 一年のカレンダーを辞書型にする
# 引数：年
# 戻り値: cal_dic
def storeCalYear(year):
    '''例: dic2017 = storeCalYear(2017)'''
    cal_dic = {}
    dotw = calcDotw("Sat",calcDaysBtwnYears(2000,year))
    for month, day_num in getMonth(year).items():
        storeCalMonth(cal_dic,month,day_num,dotw)
        dotw = calcDotw(dotw,day_num)
    return cal_dic

# カレンダーを表示する
# 引数：年、表示レイアウトを示すタプル
# 戻り値なし
# 機能：その年のカレンダーを指定したレイアウトで表示
def showCal(year,tpl):
    '''例： showCal( 2017, (3,4) )'''
    title = "Calendar "+str(year)
    print(title.center(31*tpl[0]+3))
    a_year_dic = storeCalYear(year)
    for y in range(tpl[1]): #0,1,2,3
        for a in range(8): #0~7
            for idx,m in enumerate(getMonth(year).keys()): #0,"Jan"~11,"Dec"
                if idx < tpl[0]*y: #0~11 < 3*0~3*3
                    continue
                print(" | "+a_year_dic[m][a],end="")
                if idx+1 == tpl[0]*(y+1): #0+1~11+1 == 3*1~3*4
                    print(" | ") #改行
                    break
        else:
            print()

# 実行
while True:
    try:
        year = input("What year? >")
        if year == "q": break
        tpl0 = input("How many columns? >")
        if tpl0 == "q": break
        year = int(year)
        tpl0 = int(tpl0)
        if tpl0 not in [1,2,3,4,6,12]:
            print("ERROR: invalid column number")
            print("Please enter integer that can divide 12.")
            continue
    except ValueError as e:
        print("ERROR:",e)
        print("Please enter integer number.")
        continue
    except ZeroDivisionError as e:
        print("ERROR:",e)
        print("Please enter integer larger than 0 for columns.")
        continue
    showCal(year,(tpl0,12//tpl0))
