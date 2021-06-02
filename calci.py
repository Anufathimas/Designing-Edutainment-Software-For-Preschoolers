def calc():
	print("enter first number")
	a=int(input())
	print("enter second number")
	b=int(input())
	
	selchoice=choice()
	if selchoice==1:
		sum(a,b)
		choice()
	elif selchoice==2:
		sub(a,b)
		choice()
	elif selchoice==3:
		mul(a,b)
		choice()
	elif selchoice==4:
		div(a,b)
		choice()
	else:
		print("bye")
	
	calc()
def choice():
	
	print("1.Addition") 
	print("2.substraction") 
	print("3.multiplication")
	print("4.division")
	
	print("enter your choice")
	choice=int(input())
	return choice 

		
def sum(a,b):
	sum=a+b
	print("sum=",sum)

def sub(a,b):
	sub=a-b
	print("sub=",sub)	

def mul(a,b):
	mul=a*b
	print("mul=",mul)


def div(a,b):
	div=a/b
	print("div=",div)

calc()