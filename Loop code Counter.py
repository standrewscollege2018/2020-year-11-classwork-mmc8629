"""13/2/2020 loop code counter"""
first_number = int(input(" please enter a number:"))
second_number = int(input("please enter another number:"))

if first_number < second_number:
    start = first_number
    stop = second_number
else:
    start = second_number
    

for n in range(start,stop+1):
    print (n)


