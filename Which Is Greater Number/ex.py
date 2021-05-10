num1=int(input("Enter Your First Digit: "))
num2=int(input("Enter Your Second Digit: "))
num3=int(input("Enter Your Third Digit: "))

if num1>num2 and num1>num3 :
    print(num1,"is greater")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
else:
    print(num3,"Is Greater")
print("enter your lucky number")
output=int(input())