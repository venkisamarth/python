class Movie(object):
    def  __init__(self,title,mins,hero):
        self.title=title
        self.runtime=mins
        self.hero=hero
    def printer(self):
        print(f"Title is{self.title}\n run time is{self.runtime}\n hero is :{self.hero}")
    while True:
          title=input("enter the title of Movie:")
          mins=input("Enpter the runtime:")
          hero=input("Enter the name of the hero:")
obj=Movie()
list_movies.append(obj)
print("Movies added into the list")
print("Movie add into list")
input("Do you want to add another movies(y/N)")
if ans:='y':
    break
print("All  movies inforamation:")
for obj in list_of_movies
    obj.printer()


