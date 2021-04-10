#most objects are iterable you can perform an action for every thing making up the object
#eg letters in a string, items in a list, a key in a dictionary

my_list = [1,2,3]

for each_number in my_list: #each_number is a variable placeholder you choose
    #do something with each item
    print(each_number)

    #you can also add some control flow
    if each_number % 2 == 0:
        print("its even!")
    else:
        print("its odd!")

#for loops can be used to tally

list_sum = 0

for num in my_list:
    list_sum = list_sum + num
print(list_sum)

#iterate over strings

my_string = "bob"
for my_letter in my_string:
    print(my_letter)

#python can do toople impacking
print("extracting my tooples with toople impacking")

my_list_of_tuples = [(1,2), (3,4), (5,6)]

for a,b in my_list_of_tuples:
    print(a)
    print(b)

# a lot of things return lists of tuples

#unpacking also works with dictionaries, remember dictionaries are unordered
my_dictionary = {'item1':1, "item2":2}

for my_item in my_dictionary.items():
    print(my_item)

#dictionarys can also use impacking
for my_key, my_value in my_dictionary.items(): #remember .items :O!!!
    print(my_key)
    print(my_value)

#you can also use _ as a placeholder when iterating if your not referring to an items again within your loop
my_string2 = 'something'
for _ in my_string2:
    print('we got a string')

