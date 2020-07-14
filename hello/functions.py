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
    
#pizza("chiken","fatija","mushroom","olives")


def testRetFunc(num1,num2=5):
    ans = num1 + num2
    return ans


#a = testRetFunc(1,2)
#print(a)


flag = True
items = []
while(flag):
    uIput= input("Enter food: ")
    if uIput == "Q":
        flag = False
    else:
       items.append(uIput)
print(items)


#read , write , append
with open("filename.txt","r") as file:
    content = file.read()
    
    
with open("filename.txt","w") as file:
    file.write("test data")
    
    #below mode will create and write and read file
with open("filename.txt","w+") as file:
    file.write("test data file")
    file.seek(0)
    print(file.read())
    
    


       
    
