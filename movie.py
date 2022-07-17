import pandas as pd

def all(movie):
    print(movie.to_string)

def fun_search(movie):
    search_movie = input("Search :")
    print(movie[movie["Name"] == search_movie])
    

def fun_anime(movie):
    anime_def = movie[movie["Type"] == 'Anime']
    print(anime_def.sort_values(by='Year'))

def fun_Series(movie):
    series_def = movie[movie["Type"] == 'Series']
    print(series_def.sort_values(by='Year'))

# Genre
def action(movie):
    series_def = movie[movie["Genre"] == 'Action']
    print(series_def.sort_values(by='Year'))
def scifi(movie):
    series_def = movie[movie["Genre"] == 'SciFi']
    print(series_def.sort_values(by='Year'))
def crime(movie):
    series_def = movie[movie["Genre"] == 'Crime']
    print(series_def.sort_values(by='Year'))
def Thriller(movie):
    series_def = movie[movie["Genre"] == 'Thriller']
    print(series_def.sort_values(by='Year'))
def Horror(movie):
    series_def = movie[movie["Genre"] == 'Horror']
    print(series_def.sort_values(by='Year'))
def Fantasy(movie):
    series_def = movie[movie["Genre"] == 'Fantasy']
    print(series_def.sort_values(by='Year'))
def Sport(movie):
    series_def = movie[movie["Genre"] == 'Sport']
    print(series_def.sort_values(by='Year'))
def Romance(movie):
    series_def = movie[movie["Genre"] == 'Romance']
    print(series_def.sort_values(by='Year'))
def War(movie):
    series_def = movie[movie["Genre"] == 'War']
    print(series_def.sort_values(by='Year'))
def Kids(movie):
    series_def = movie[movie["Genre"] == 'Kids']
    print(series_def.sort_values(by='Year'))

def fun_genre(movie):
    genre_choice = 100
    while(genre_choice !=11):
        print("\nGenre : 1)Action 2)SciFi 3)Crime 4)Thriller 5)Horror 6)Fantasy 7)Sport 8)Romance 9)War 10)Kids 11) Exit --->\n")
        genre_choice = int(input())
        if(genre_choice==1):
            action(movie)
        elif(genre_choice==2):
            scifi(movie)
        elif(genre_choice==3):
            crime(movie)
        elif(genre_choice==4):
            Thriller(movie)
        elif(genre_choice==5):
            Thriller(movie)
        elif(genre_choice==6):
            Fantasy(movie)
        elif(genre_choice==7):
            Sport(movie)
        elif(genre_choice==8):
            Romance(movie)
        elif(genre_choice==9):
            War(movie)
        elif(genre_choice==10):
            Kids(movie)
            
def fun_year(movie):
    year = int(input("Year :"))
    print(movie[movie["Year"] == year])
    
movie = pd.read_excel('list_of_movie.xlsx')
choice=100
while(choice!=5):
    print("\n\n\n<---------------Welcome to Panda Movies --------------->\n")
    choice=int(input('''Menu: 0)Search 1)Anime 2) Web Series 3) Genre 4)Year 5)exit --->'''))
    if (choice==0):
        fun_search(movie)
    elif(choice==1):
        fun_anime(movie)
    elif(choice==2):
        fun_Series(movie)
    elif(choice==3):
        fun_genre(movie)
    elif(choice==4):
        fun_year(movie)
