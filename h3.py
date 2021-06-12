class Countpgm:
	count=0
	def __init__(self,count):
		self.count=count
		Countpgm.count=Countpgm.count+1
ct1=Countpgm(1)
ct2=Countpgm(2)
ct3=Countpgm(3)
ct4=Countpgm(4)
ct5=Countpgm(5)
print("no of object=",Countpgm.count)
