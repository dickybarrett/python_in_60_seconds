#counter
i = 1

#looping logic
while i < 101:

    #tackle fizzbuzz first
    if i % 3 ==0 and i % 5 ==0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    #end of loop
    i = i + 1