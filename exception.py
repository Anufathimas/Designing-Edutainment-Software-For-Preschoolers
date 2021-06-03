def myfunction():
    try:
        num=10/0
        print(num)
    except:
        print("something went wrong")
    c=2+3
    print(c)



def myfunctionarray():
    try:
        num=10/0
        print(num)
    except:
        print("something went wrong")
    finally:
        num=10
        print(num)
        print("exception completed")
    c=2+3
    print(c)

myfunctionarray()
