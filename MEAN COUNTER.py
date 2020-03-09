"""exorcise 2 26/2/20 mean counter"""

number = []

keep_asking = True

while keep_asking == True:
    num = int(input("Enter a number :"))
    if (num) == -1 :
        keep_asking = False
            
    else:
        number.append (num)
for i in range(len(number)):
    print(number[i])                
            
print("the sum of those numbers are",sum (number))
            
    
        

