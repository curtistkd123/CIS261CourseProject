

def fibonnaci (sequencenumber):
    num1, num2 = 0, 1
    count = 0

    if sequencenumber <= 0:
        print("Please enter a positive integer")

    elif sequencenumber == 1:
        print("Fibonacci sequence upto",sequencenumber,":")
        print(num1)

    else:
        print("Fibonacci sequence:")
        while count < sequencenumber:
            print(num1)
            temp = num1 + num2
            
            num1 = num2
            num2 = temp
            count += 1

sequencenumber = int(input("How many sequences? "))
fibonnaci(sequencenumber)