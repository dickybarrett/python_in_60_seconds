#good for repeatable blocks of code

#def keyword

def my_function(int1,int2):
    result = int1+int2
    return result

print(my_function(1,2))

#basic functions

def say_hello():
    print('hello')
    
say_hello()

#you cannot call it without parenthesis, you must include them

#input arguments

def say_hello(name='Default'): #you can provide default values with =
    print(f'hello {name}')
    
#usually with functions your returning a value

def div_nums(num1, num2):
    return num1/num2 #returns a value

print(div_nums(2,3))

#you should check data types passed in
def some_numbers(num1, num2):
    return num1+num2
