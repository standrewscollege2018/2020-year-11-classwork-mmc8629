"""raffle"""

print("welcome to the raffle roller bot") 

import random

raffle = []
illegal = set("0123456789?/.>,<:;}]{[=+-`'_)0(9*8&7^6%5$4#3@2!1~")



get_item = True
while get_item==True:
      raffle_item = input("what prize would you like to be in the raffle ?  ")
      if raffle_item == "":
            print("ENTER A NAME")
      else:
            get_item = False
#make a loop to ask for a number

raffleprice = True
while raffleprice == True:
      try:
            raffle_price = int(input("please enter the price of the goods: $"))
      except ValueError:
            print("ERROR please enter a valid number")
      else:
            raffleprice = False
      
keep_asking = True
      
while keep_asking == True:
      name = input("please enter a name: ")
      # use .lower() to handle capitalisation
      if name.lower() == "stop":
            keep_asking = False
      elif name=="":
            print("NO INPUT")
      elif name.lower() in raffle :
                  print("Please enter another name, this name has already been taken")
      elif any((c in illegal) for c in name):
            print("ERROR, Please enter a valid name")
                       
      else:
            raffle.append(name.lower())
            
            
for i in range(len(raffle)):
      print(i+1, raffle[i])
      
winner = random.randint(0,len(raffle)-1)

print("the winner is {} winning {}!".format(raffle[winner], raffle_item))
print("!CONGRATULATIONS!")
    
    
    
    


    




