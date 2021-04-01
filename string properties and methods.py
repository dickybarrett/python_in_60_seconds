#strings are immutable - they cannot mutate or change

name = "sam"

#name[0] = 'p' doesnt work
#you must create a new string or concatonate them

#you could use slicing to grab the part of the string
#you need

lastletters = name[1:] #start at index 1 and go all the way to the end

#string concatonation
name = "P"+lastletters

print(name)

print(name * 10)

#objects have built in methods
mystring = "hello there"

mystring = mystring.upper()

print(mystring)

mystring = mystring.split()
print(mystring)

#interpolation using the format keyword
str1 = 'my'
str2 = 'string'
print("this is {} {}".format(str1,str2))
print('you can also do it {1} {0}'.format('way','this')) #passing in a list

#or even
print("the {q} {b} {f}".format(q='quick',b='brown',f='fox'))

# .format is also really useful for dealing with large floating point results
result = 997 / 222
print('the result was {r:1.3f}'.format(r=result))

#next f strings from python 3.6
name = 'rich'
print(f'hello {name}')


