#logic in python functions

#combine our logic knowledge and our function knowledge

#a function to test for evenly divisible by an operator

def isitdivisible(targetnumer, divider):
    if targetnumer % divider == 0:
        return True
    else:
        return False
    
print("Testing 10/2 to see of it is even: {}".format(isitdivisible(10,2)))

#you can also pass in lists


numlist =  [1,2,3,4,5]

def isitdivisible2(targetlist, divider):
    
    even_numbers = []
    
    for number in targetlist:
        if number % divider == 0:
            even_numbers.append(number)
        else:
            pass #pass means dont do anything we only care for true

    return even_numbers


list_even = isitdivisible2(numlist,2)

print(list_even)