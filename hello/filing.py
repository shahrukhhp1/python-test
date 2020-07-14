    #below mode will write and read file not create
#with open("filename.txt","r+") as file:
#    file.write("test data file")
#    file.seek(0)
#    print(file.read())


  #below mode will create , write and read file 
#with open("filename2.txt","w+") as file:
#    file.write("test data file somother test")
#    file.seek(0)
#    print(file.read())

#append text
#with open("filename.txt","a") as file:
#    file.write(" appending")
#    file.seek(0)

#with open("filename.txt","r") as file:
#    print(file.read())


import csv





with open("a.csv","a",newline="") as f:
    handeler = csv.writer(f,delimiter=",")
    handeler.writerow(["test","test2","test4"])
    


with open("a.csv") as f:
    data = csv.reader(f)
    for line in data:
        print(line)
