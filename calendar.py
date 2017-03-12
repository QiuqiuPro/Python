week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
first_day = "Wed" #Depends on what month you are in.
today = int(input("What is the date today?"))
n = ( week.index(first_day) + (today % 7 - 1) ) % 7
print("Today is {0}".format(week[n]))
