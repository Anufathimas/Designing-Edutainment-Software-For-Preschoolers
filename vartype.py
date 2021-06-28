                            

carmodel= 34501              # carmodel is of type int  :global variable         
gear = 0                     # gear is of type int : global variable
carcolor="white"             # carcolor is of type string : global variable

def carStart():

  gear= 0         # declaring and intializing  local variable gear 
  gear= gear+1    # calling local variable gear and increment with 1     (here since a local variable gear is creted it will only call local variable instead of global variable 
  print("car start gear=",gear)
  carcolor="red"  # local variable of carStart()
  print("car color=",carcolor)
  print ("carmodel=",carmodel)   # calling global variable carmodel

class MyCar:

    speed =0    #class variable

 
    def __init__(self,carusername,carpassword):    # declaring init fuction with parameters carusername and carpassword
            self.cname = carusername                    # intializing instance variable cname with value passed from carusername
            self.cpassword = carpassword                # intializing instance variable cpassword with value passed from carpassword
            print("welcome user ,carusername") 

    def carRun(self):

        print("current gear",gear)     
        MyCar.speed = input("enter your speed")    # calling class variable speed and  assign value via user input 
        print("current speed",MyCar.speed)
        music=input("enter music on or off:1 for on ,0 for off")  # calling local variable music and assign value via user input 
        print("music ststus=",music)

carStart()
benz=MyCar("eric","car123")
benz.carRun()

