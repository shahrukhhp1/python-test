fruits = ['ca', 'at', 'ddd', 'cd', 'ab', 'appl', 'a']


##for i in range(0,15,3):
##    print(i)

## print reverse list and reversed text
for i in range(len(fruits)):
    index = len(fruits) - i
    item = fruits[index - 1];
    ##print(item)
    ##print(len(item))
    toPrint=''
    for b in range(len(item)):
        lIndex = len(item) - b - 1
        toPrint+=item[lIndex]
    print(toPrint)
## hurray



##
##for elem in fruits:
##    print(elem)
##    if elem == 'appl':
##        break
##print('done')
##
##
##


#lists
fruits = ['ca', 'at', 'ddd', 'cd', 'ab',23, 'appl', 'a']
ab = fruits.index('appl')
print(ab)

print(fruits[1:4]) # slice

del fruits[1]



print(fruits)



fruits.remove('ab')



print(fruits)

print(fruits.pop())

print(fruits)

print(len(fruits))


