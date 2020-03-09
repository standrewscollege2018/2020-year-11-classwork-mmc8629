"""while loop"""
#import the random code from python
import random

# set the random number as a varible
num = random.randint(1,10)

#set the varible to start asking
keep_asking = True

#start code with the asking varible
while keep_asking == True:
    #make the persons guess a varible
    guess = int(input("enter a number between 1 to 10 : "))
    #make it so if the ranom number created is equel to the persons guess make it so the code stops
    if guess == num : 
        print("thats right")
        keep_asking = False
    #and if its not right it needs an elif and to check if its higher or lower
    elif guess < num:
        #and it desplays if it is higher or lower
        print("try something higher")
    
    elif guess > num:
        print("try something lower")
        


        
