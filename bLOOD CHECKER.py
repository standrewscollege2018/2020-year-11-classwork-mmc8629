"""11/2/20 blood doner task"""
#set minimum child age constant
CHILD_AGE = 16
#set minimum weight limit
WEIGHT_LIMIT = 50

#ask for their age and weight
age = int(input("How old are you: "))
weight = int(input("What is your weight: "))


#check their age and weight
if age < CHILD_AGE or weight < WEIGHT_LIMIT:
    print("Sorry but you are unable to donate")
    
else:
    print("you are able to donate")