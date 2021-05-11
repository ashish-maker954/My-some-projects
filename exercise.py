list1 = {1:"Ashish",2:"Harshit",3:"shivang",4:"Adarsh"}
list2 = {1:"Exercise",2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select client name :")
    for num,nam in list1.items():
        print("press",num ,"for" ,nam,"\n",end="")
    username=int(input())
    print("Selected client : ",list1[username],"\n",end="")

    print("press 1 for lock")
    print("press 2 for retrive")
    op=int(input())

    if op is 1:
        for key, value in list2.items():
            print("Press", key, "to lock", value,"\n", end="")
        lock_name =  int(input())
        print("Selected Job : ", list2[lock_name])
        f = open(list1[username] + "_" + list2[lock_name] + ".txt", "a")
        k = 'y'
        while(k is not "n"):
            print("Enter", list2[lock_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n: ")
            continue
        f.close()
    elif op is 2:
        for key, value in list2.items():
            print("Press", key, "to retrieve", value,"\n", end="")
        lock_name =  int(input())
        print(list1[username], "-", list2[lock_name], "Report :","\n", end="")
        f = open(list1[username] + "_" + list2[lock_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close() 
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")    
