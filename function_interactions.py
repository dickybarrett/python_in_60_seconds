#functions can interact with each other

#three cup monty, a red ball hidden under one cup, guess where the ball is

#python list two empty strings, one containing an o for our ball

example_list = [1,2,3,4,5]

from random import shuffle #import a library


#Game logic here 



def player_guess(): 
    guess=''
    
    while guess not in ['0','1','2']: #not in ultra useful
        guess = input("Pick a number: 0,1 or 2")
        return int(guess)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

   
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess')
        print(mylist)
        
# A list representing three cups, one with ball O
mylist = ['','O','']

#shuffle
mixed_up_list = shuffle_list(mylist)

#take user guess
guess = player_guess()

#combined shuffled list and user guess and check it
check_guess(mixed_up_list, guess)

