from movies import Movies
movies = Movies('./movies.txt')


print("menu:")
print("sn: Search movie name")
print("sc: Search cast name")
print("list: list all movies")
print("q: quit")
print()
def list():


def iscast():

def ismoviename():


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
        
   