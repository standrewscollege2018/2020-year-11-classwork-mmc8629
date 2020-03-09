
"""19/2/2020 trademe code"""

item = input("what would u like to sell?: ")
 
reserve_price = int(input("what would you like the item to go for?: "))
highest_price = 0
highest_name = "Jesus Jimminy Christmas"
reserve_met = 0
 
auction_run = True
 
while auction_run == True :
  name = input("please enter your name: ")
  price = int(input("please enter your bid: "))
  
  if highest_price >= reserve_price and reserve_met == 0 :
    print("reserve has been met")
    reserve_met = 1
    
  elif price >  highest_price : 
    highest_price = price
    highest_name = name
    print("The highest bid so far is {} at {}".format(highest_name,highest_price))
  
  else:
    print("That is not high enough.")
    print("The highest bid so far is {} at {}".format(highest_name,highest_price))
    

    

  
  
  
 


             