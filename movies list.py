"""movie list"""
#set up list to store movies
movies = []

#print greeting
print("enter your 3 favourite movies of all time, in order form most favourte to least")

# start loop for only 3 times

        
        
keep_asking = True 
while keep_asking == True :
    movies_name = input("Enter a favourite movie: ")
    if movies_name == "stop" :
        keep_asking = False
    else :
        movies.append(movies_name)
print(movies)

# loop through list and display the movies nicely 
for movie in movies:
    print (movie)
    
for i in range(len(movies)):
    print(i+1, movies)






    



