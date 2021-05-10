output = input("enter your name   ")
print("Welcome", output,"u will give your class standard in which you study\n To know that you are in Primary,Junioror senior secondry" )

standard = int(input("enter your class   "))

if standard <6 and standard>1:
     print("you are in primary") 

if standard ==1:
     print("you are in primary") 

if standard <12 and standard>8:
     print("you are in seniour secondry") 

if standard >13:
     print("not a valid class")

elif standard<9 and standard >5:
      print("you are in junior")