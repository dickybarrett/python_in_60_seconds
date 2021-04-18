
#quick way to create a list a good alternative to using a for loop to create a list

mystring = 'hello'

mylist = []

for eachletter in mystring:
    mylist.append(eachletter)


#better way to do this in python, computation is the same but more efficient in code

mylist2 = [letter for letter in mystring] #element for element in mystring

print(mylist2)

#also works with numbers using range
mylist3 = [num for num in range(0,100)]
print(mylist3)

#even math
mylist3 = [num*2 for num in range(0,100)] #also good for conversions
print(mylist3)

#can also add in an if
mylist = [x for x in range(1,101) if x % 2 == 0]
print(mylist)

