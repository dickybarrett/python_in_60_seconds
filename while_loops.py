#execute a block of code while a condition remains true

#while dogs are hungry keep feeding them, usually uses some boolean condition
#can be combined with else

x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print(f"{x} is not less than 5")


#break continue and pass
#break breaks out of the loop
#continue goes to the top of the loop
#pass does nothing at all

x = [1,2,3]

for item in x:
    #you will get an error with no logic here due to python whitespace
    #so we use pass as a placeholder for logic
    pass

mystring = "bob"

#continue used to skip a condition
for eachletter in mystring:
    if eachletter == 'b':
        continue #continue can be used to skip a condition
    print(eachletter)


x = 5

while x < 5:
    if x == 4:
        break #break is a get out condition
    
    print(x)
    x += 1

