print("{0:=^41}".format("begin"))

# let user input year
year_dic = {}
year=int(input("What year? \n"))
leap_year = (year %400 == 0) or ((year %4 == 0) and (year %100 != 0))
if leap_year == True:
    year_dic[year] = ["( Leap )", 29]
    #print("{0:-^29}\n|  {1:>11} {2:<12} |\n{3:-^29}".format("",year,"Year","(Leap)"))
else:
    year_dic[year] = ["( Normal )", 28]
    #print("{0:-^29}\n|  {1:>12} {2:<12} |\n{3:-^29}".format("",year,"Year ","-(Normal)"))
print("\n{0:-^29}\n|  {1:>11} {2:<12} |\n{3:-^29}".format("",year,"Year",year_dic[year][0]))
weekyobi = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# 2000.1.1 first_2000 = "Sat"

def leap_times(x):
    return x//4 - x//100 + x//400
    # 1~x Leap year times: x//4 - x//100 + x//400
leap_times = leap_times(2000)-1 - leap_times(year-1)
first_day_year = weekyobi[(year + 1 - leap_times) % 7]

# The input year's calendar
monlist = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
#days_feb : days of feberary

mon_dic = {'Jan.': 31, 'Feb.': year_dic[year][1], 'Mar.': 31, 'Apr.': 30, 'May': 31, 'Jun.': 30, 'Jul.':
31, 'Aug.': 31, 'Sep.': 30, 'Oct.': 31, 'Nov.': 30, 'Dec.': 31}
#print(mon_dic)

first_day = first_day_year # first day of the year.

# the last day of the last month
last_months_last_day = 0
for mm in range(0,12):
    print("\n{0:^29}".format(monlist[mm]))
    for yobi in weekyobi:
        print("{0:>4}".format(yobi),end="")
    print()
    last_months_last_day = mon_dic[monlist[mm]]
    # first day's yobi
    fdy = weekyobi.index(first_day) # what yobi the first day of this year is
    for j in range(0, fdy):
        print("{0:>4}".format(""),end="")
        # print out the lastest some days in the first week of the month
        #print("{0:>4}".format(last_months_last_day-fdy+1+j),end="")
    for i in range(0,last_months_last_day):
        if (i+fdy-1)%7 == 6:
            print()
        print("{0:>4}".format(i+1),end="")
    print()
    x = (last_months_last_day + fdy)%7
    first_day = weekyobi[x]

print("\n{0:=^41}".format("end"))
