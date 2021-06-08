def view():
	print("Enter a limit")
	n=int(input())
	selchoice=choice()
	if selchoice==1:
		hai(n)
		choice()
	elif selchoice==2:
		bye(n)
		choice()
	else:
		print("bye")
	view()
def choice():
	print("1.Forward")
	print("2.Backward")
	print("enter your choice")
	choice=int(input())
	return choice

def hai(n):
	i=1
	while(i<=n):
		print(i)
		i=i+1
def bye(n):
	i=n
	a=1
	while(i>=a):
		print(i)
		i=i-1

view()