#useful built in functions and operators in python

#the range function
#instead of creating a list of numbers we can use the range function
#its iterable

for num in range(10):
    print(num) #up to but not including 10

for num in range(3,10):
    print(num)

for num in range(3,10,2): #include step size
    print(num)

#range is a generator you can cast it to a lisst

mylist = list(range(0,11,2))

print(mylist)

#====================================================

#enumeration

index_count = 0

for letter in 'abc':
    print('at index  {} the letter is {}'.format(index_count, letter)) #feeds index count and letter back into the string
    index_count += 1

#usually you will want a counter for how many times you have gone through a for loop or to know which position you at

index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1

#or

for index,letter in enumerate(word): #enumerate returns tuples so we leverage tuple unpacking here
    print(index, letter)

# join two lists in a zip function
#you got to iterate with it

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for myItem in zip(mylist1,mylist2): #joins list ignores extras
    print(myItem) #returns a tuple which can be unpacked, 

#can also cast zip to a list
newlist = list(zip(mylist1, mylist2))
print(newlist)

#in operator to check a list
'x' in ['x','y','z'] #returns true as x is there also works on dictionaries for keys and strings

mylist = [10,20,30,40]

print(min(mylist)) #min returns min value

print(max(mylist)) #max returns min value

#python has a random library we have to import the library

from random import shuffle

mylist = [1,2,3,4]

shuffle(mylist)

print(mylist)

from random import randint #get a random integer

myint = randint(0,100)

print(myint)

#accepting user input
result = input('enter a numer: ') #accepts a value as a STRING!
int(result)
print(result)

