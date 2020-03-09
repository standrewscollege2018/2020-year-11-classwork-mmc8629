"""11/2/2020 zoo"""
#set child age limit for later
CHILD_AGE = 13
#get the age from the user 
age = int(input("How old are you?: "))
#check to see if child is young enough
if age < CHILD_AGE:
    print("You pay the child price")
#check to see if child is too old
if age > CHILD_AGE or age == CHILD_AGE:
    print("you will will need the child pass")
print ("welcome to the Zoo")
print ("please pay here")



