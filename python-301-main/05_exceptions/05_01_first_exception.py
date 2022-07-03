# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.
while True:
    try:
        ask=int(input(f"From 0 to 10, how big is your hunger? "))
        if 0<ask<5:
            print(f"You can eat something small and healthy until next meal")
            break
        elif 11>ask>=5:
            print(f"You can go for a full meal")
            break
        else:
            raise Exception 
    except ValueError:
        print("please put numbers")
        continue
    except Exception:
        print("numbers between the range please")
        continue


