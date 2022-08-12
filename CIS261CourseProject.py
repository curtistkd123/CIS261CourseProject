print("Hello World")
date = ""

while date != "a-1":
    
    date = input("enter a date or a-1 to end program")
    if date == "a-1":
        print("Goodbye")
        break

    my_tokens = date.split()
    print(my_tokens)
    print(my_tokens[0])
    print(my_tokens[1])

    if my_tokens[0] == "January" or my_tokens[0] =="Jan" or my_tokens[0] =="1" or my_tokens[0] =="01":
        date = "1"
    elif my_tokens[0] == "February" or my_tokens[0] =="Feb" or my_tokens[0] =="2" or my_tokens[0] =="02":
        date = "2"
    elif my_tokens[0] == "March" or my_tokens[0] =="Mar" or my_tokens[0] =="3" or my_tokens[0] =="03":
        date = "3"
    elif my_tokens[0] == "April" or my_tokens[0] =="Apr" or my_tokens[0] =="4" or my_tokens[0] =="04":
        date = "4"
    elif my_tokens[0] == "May" or my_tokens[0] =="may" or my_tokens[0] =="5" or my_tokens[0] =="05":
        date = "5"
    elif my_tokens[0] == "June" or my_tokens[0] =="Jun" or my_tokens[0] =="6" or my_tokens[0] =="06":
        date = "6"
    elif my_tokens[0] == "July" or my_tokens[0] =="Jul" or my_tokens[0] =="7" or my_tokens[0] =="07":
        date = "7"
    elif my_tokens[0] == "August" or my_tokens[0] =="Aug" or my_tokens[0] =="8" or my_tokens[0] =="08":
        date = "8"
    elif my_tokens[0] == "September" or my_tokens[0] =="Sept" or my_tokens[0] =="9" or my_tokens[0] =="09":
        date = "9"
    elif my_tokens[0] == "Ocotober" or my_tokens[0] =="Oct" or my_tokens[0] =="10":
        date = "10"
    elif my_tokens[0] == "November" or my_tokens[0] =="Nov" or my_tokens[0] =="11":
        date = "11"
    elif my_tokens[0] == "December" or my_tokens[0] =="Dec" or my_tokens[0] =="12":
        date = "12"
    else:
        print("Please input correct month number or full month name or 3 letter month")
        continue

    if(my_tokens[1].__contains__(",")):
        my_tokens[1] = my_tokens[1:-1]

    x = int(my_tokens[1])
    if date == "2" and x > 29:
        print("there is only a max of 29 days in February")
        continue
    if (date == "1" or date =="3" or date == "5" or date == "7" or date == "8" or date == "10" or date == "12") and x > 31:
        print("there cant be more than 31 days in the month inputed")
        continue
    if (date == "4" or date =="6" or date =="9" or date =="11") and x > 30:
        print("there cant be more than 30 days in the month inputed")

    yr = int(my_tokens[2])
    if yr < 1000 or yr > 9999:
        print("Please use a 4 digit year")
        continue

    date +="/"+str(x)+"/"+str(yr)

    print(date)
