num1 = input("check whether happy number innit")

def happyCheck(num1: str): 
    
    pass
    

def checkFile(num1):
    with open("happynumber","r") as file:
        numbers = file.readline().split(",") 
    for i in numbers:
        number = int(i)
        if number == num1: 
            return True
    return False    

def addFile(num1):
    number = 0
    if happyCheck(num1) == True: 
        
        with open("happynumber","a") as file:
            for i in num1: 
                number += (num1[i])**2 
                file.write(","+number)   

