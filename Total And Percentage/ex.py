sub1=int(input("Enter the first subject marks: "))
sub2=int(input("Enter the second subject marks: "))
sub3=int(input("Enter the third subject marks: "))

total=sub1+sub2+sub3
per=total/3
print("Total number marks is: ",total)
print("Percentage is: ",per )

if total>300:
    print("marks will be taken under 100 only")

print("enter your lucky number")
output=input()