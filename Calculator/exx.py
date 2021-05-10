def division():
    try:
        y = "Enter your 1st number: "
        z = "Enter your 2nd number: "
        n1=int(input(y))
        n2=int(input(z))
        print("Ans: ", int(n1/n2))
    except Exception as e:
        e="Invalid Input"
        print(e)
        pass
def subtraction():
    try:
        a="enter your 1 number"
        b="enter your 2 number"
        n1=int(input(a))
        n2=int(input(b))
        print("Ans: ",int(n1-n2))
    except Exception as y:
        y="Invalid Input"
        print(y)
        pass   
def Addition():
    try:
        a="enter your 1 number"
        b="enter your 2 number"
        n1=int(input(a))
        n2=int(input(b))
        print("Ans: ",int(n1+n2))
    except Exception as p:
        p = "Invalid Input"
        print(p)
        pass
def multiplication():
    try:
        y="enter your 1 number"
        z="enter your 2 number"
        n1=int(input(y))
        n2=int(input(z))
        print("Ans: ",int(n1*n2))
    except Exception as j:
        j="Invalid Input"
        print(j)
        pass
def modulo():
    try:
        y="enter your 1 number"
        z="enter your 2 number"
        n1=int(input(y))
        n2=int(input(z))
        print("Ans: ",int(n1%n2))
    except Exception as k:
        k="Invalid Input"
        print(k)
        pass
def floor_division():
    try:
        y="Enter your 1 number"
        z="Enter your 2 number"
        n1=int(input(y))
        n2=int(input(z))
        print("Ans: ",int(n1//n2))
    except Exception as l: 
        l="Invalid Input"
        print(l)
        pass
def exponent():
    try:
        y="Enter your 1 number"
        z="Enter your 2 number"
        n1=int(input(y))
        n2=int(input(z))
        print("Ans: ",int(n1**n2))
    except Exception as n:
        n="Invalid Input"
        print(n)
        pass
def cal():
    while True:
        print("\t(+): Addition \n \t(-): Subtract \n \t(*): Multiplication \n \t(/): Division \n \t(%): Modulo \n \t(//): Floor Division \n \t(**): Exponentiation \n\t($): Exit")
        x=input("What you wanted to do? ")
        if(x=="+"):
            Addition()
            continue
        elif(x=="-"):
            subtraction()
            continue
        elif(x=="*"):
            multiplication()
            continue
        elif(x=="/"):
            division()
            continue
        elif(x=="%"):
            modulo()
            continue
        elif(x=="//"):
            floor_division()
            continue
        elif(x=="**"):
            exponent()
            continue
        elif(x=="$"):
            print("See You Later")
            output=int(input("Enter your favourite number"))
            break
        else:
            print("Invalid Input")
                
cal()


