while True:
    user_input = input("////////////\nenter number\n////////////\n>>")
    if (user_input == "") or (user_input == ".") or (user_input == "q"):
        break
    try:
        num1 = int(user_input)
    except ValueError:
        print("ValueError. please enter number only")
        continue
    except:
        import traceback
        traceback.print_exc()
        continue
    print("{0}^2={1}".format(num1, num1 ** 2 ))
