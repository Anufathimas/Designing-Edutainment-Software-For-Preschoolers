class Mylibrary:
    def __init__(self,bookname,bookauthor):
        self.mybookname=bookname
        self.mybookauthor=bookauthor
        print("my library object created with instance variables: mybookname and mybookauthor")
cetlibrary=Mylibrary("wings of fire"," a p j")
lourdelibrary=Mylibrary("my experience","gandhi")
#print(cetlibrary.mybookname,cetlibrary.mybookauthor)
#print(lourdelibrary.mybookname,lourdelibrary.mybookauthor)
 
librarylist=[]
librarylist.append(lourdelibrary)
librarylist.append(cetlibrary)

print("arrayobject librarylist created with two objects cetlibrary in position 0 and lourdelibrary in position 1")

for x in librarylist:
    print(x.mybookname,x.mybookauthor)
