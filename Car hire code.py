"""Car Rental """


cars = [["Suzuki Van", 2, True], ["Toyota Corolla", 4, True], ["Honda CRV", 4, True], ["Suzuki Swift", 4, True], ["Mitshibishi Airtrek", 4, True], ["Nissan DC Ute", 4, True], ["Toyota Previa", 7, True], ["Toyota Hi Ace", 12, True], ["Toyota Hi Ace", 12, True]]

day_keeprunning = True

while day_keeprunning == True:
   
   # get the number of seats the user needs
   seats  = int(input("How many seats do you require? "))
   if seats == 0:
      break
   # loop through the liSt of cars
   for n in range(0,len(cars)):
      # only display names of cars that have enough seats and are available (cars[n][2]=True)
      if cars[n][1] >= seats and cars[n][2]==True:
         # print a number and the car name
         print(n+1,cars[n][0])
   # user selects the car they want by entering a number
   selection = int(input("What car do you want?"))
   # change the availabiltiy of the car they selected to False
   cars[selection-1][2] = False
   
print(cars)        
      
      
      
      
         
   
    
    
