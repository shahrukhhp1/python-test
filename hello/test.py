import models as m
import sqlRepo as repo



def Main():
    repo.DBTestFunction()
    
    #TestFunc3()
    


def TestFunc3():
    a= " abc" * 4
    print(a)
    print(len(a))



def testFunc():
    arr= ['abc','cde','efg']
    print(arr[1])
    print(len(arr))
    print(arr)

    for x in arr:
        print(x) 


class myclass:
    x=1
    y="fahim"

def testFunc2():
    a = myclass()
    a.x=5

    print(a.x,a.y)

    theList=[]
    for x in range(10):
        id = x
        num = x * 321
        name = "fahim" + str(num)

        d = m.Patient(id,num,name)
        theList.append(d)


    # print(d.Name,d.CellNumber,d.Id)
    print(len(theList))
    selected = None
    for x in theList:
        if(x.Id == 3):
            selected = x
            break



    print(selected.CellNumber)



Main()