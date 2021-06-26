class Car():
	x=5
	n=10
	def _init_(self,n,m):
		self.n=n
		self.m=m
	def hai(self):
		print("this is car")
	def hello(self,colour):
		print("this is color",colour)
	def view(self,colour,number):
		print("this is number",number,colour)
	
	
w=Car(7,8)
print(w.n)
p=Car()
p.hai()
p.hello("red")
p.view("red",6)
print(p.x)
p.x=p.x+1
print(p.x)
q=Car()
print(q.x)


	
	