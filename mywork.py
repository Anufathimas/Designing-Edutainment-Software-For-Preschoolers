class Mywork:
    def student(self):
        studname=input("enter a name : ")
        idno=input("enter an ID : ")
        email=input("enter a email : ")
        try:
            filename=input("enter file name: ")
            doc=open("C:/Users/anuzd/Desktop/python/file/"+filename,"a")
            filedata="name="+studname+"\n ID="+idno+"\n email="+email
            doc.write(filedata)
            doc.close()
        except:
            print("file already exisit")
            filename=input("enter new file name")

            doc=open("C:/Users/anuzd/Desktop/python/file/"+filename,"a")
            filedata="name="+studname+"\n ID="+idno+"\n email="+email
            doc.write(filedata)
            doc.close()


        
        doc=open("C:/Users/anuzd/Desktop/python/file/"+filename,"r")
        print(doc.read())
        doc.close()

w1=Mywork()
w1.student()