def inputInt():
    ''' ask user to input int number. if value  '''
    while True:
        user_input = input("////////////\nenter number\n////////////\n>>")
        if (user_input == "") or (user_input == ".") or (user_input == "q"):
            break
        try:
            num1 = int(user_input)
            break
        except ValueError:
            print("ValueError. please enter number (int) only")
            continue
        except Exception as e:
            print("Unexpected Error:", e)
            continue
    return num1

def inch_to_cm(inch):
    return round( inch * 2.54, 2 )
