

def factorial (num):
    factorials = []
    ans = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("0! = 1")
    else:
        x = 1
        while x <= num :
            factorials.append(x)
            x+=1

        for f in factorials:
            ans *= f
        
        print (str(num)+"! = "+str(ans))

def factorialRec (test,count):
    if count < len(test):
        num = test[count]
        factorials = []
        ans = 1
        if num == 0:
            print("0! = 1")
        else:
            x = 1
            while x <= num :
                factorials.append(x)
                x+=1
            for f in factorials:
                ans *= f
            print (str(num)+"! = "+str(ans))

        factorialRec(test,count+1)


test= [0,5,10,25,50,100]
print("Factorial results using interative function")
for x in test:
    factorial(x)

print("Factorial results using recursive")
factorialRec(test,0)