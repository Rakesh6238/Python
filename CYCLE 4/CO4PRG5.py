class publisher:
    def __init__(self,n):
        self.name=n
    def display(self):
        print("name of publisher",self.name)
class book(publisher):
    def __init__(self,n,t,a):
        super().__init__(n)
        self.title=t
        self.author=a
    def display(self):
        print("title of book",self.title)
        print("author of book",self.author)
class python(book):
    def __init__(self,n,t,a,p,np):
        super().__init__(n,t,a)
        self.__price=p
        self.__no_pages=np
    def display(self):
        print("name of publisher",self.name)
        print("title of book",self.title)
        print("author of book",self.author)
        print("price",self.__price)
        print("pages of book",self.__no_pages)
new=python("Dc Books","python1","ravi",100,230)
new.display()



