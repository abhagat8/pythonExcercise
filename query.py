from movies import Movies
movies = Movies('./movies.txt')


print("menu:")
print("sn: Search movie name")
print("sc: Search cast name")
print("list: list all movies")
print("q: quit")
print()

def list():
    for i in range (0, len(movies._movies), 1):
        print(movies._movies[i]['name'])

def iscast():


def ismoviename():
    checkname=input("enter the movie name: ").lower()
    for i in range(0, len(movies._movies), 1):
        if(movies._movies[i]['name'].lower().__contains__(checkname.lower())):
            print(movies._movies[i]['name'])

x=True
while x:
    print("menu:")
    print("sn: Search movie name")
    print("sc: Search cast name")
    print("list: list all movies")
    print("q: quit")
    print()
    choice=input("enter your input: ")
    if(choice== "sn"):
        ismoviename()
        
    elif(choice== "sc"):
        iscast()
        
    elif(choice== "list"):
        list()
        
    elif(choice== 'q'):
        x=False
        
   