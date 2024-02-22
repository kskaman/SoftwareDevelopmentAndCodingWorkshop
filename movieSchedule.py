# Gets a movie from user and gives the time  the movie is going to be played

moviesSchedule = {'Spiderman': '8 am', "Oppenhemeir" : "11:30 am", "John Wick": "2 pm", "Barbie" : '4:30 pm', "Jungle" : "7 pm"}



print("We are playing following movies today : ")
for k in moviesSchedule.keys():
    print(k)

movie = input("\nWhat movie you want to watch : ").strip()

if movie in moviesSchedule.keys():
    print(movie + " will be played at " + moviesSchedule[movie] + " in the theatre.\n")
else :
    print("Sorry, we are not plyaing " + movie + " today.\n")