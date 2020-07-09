def  add():
    print(1+2)
    
    
#add()


def  add(num1,num2): #parameterized func
    print(num1+num2)
    
    
#add(1,4)



def  fullname(firstName,lastName): 
    print(firstName + lastName)
    
    
#fullname(lastName="test",firstName="abb") #keyword arguments


def testFunc(num1,num2=5):
    print(num1 + num2)
    
#testFunc(5)


def pizza(name,flavour,*toppings): #arbitary arguments with star sign
    print(f"you have ordered {name} pizza with flavour {flavour} with top {toppings}")
    
pizza("chiken","fatija","mushroom","olives")