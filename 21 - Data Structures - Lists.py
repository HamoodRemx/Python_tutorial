################################################################
######################## Define Lists ##########################
################################################################
# region

# Lists is build-in data structure, we use square brackets to define a list of a sequence of object with different types.
# We can a list of strings, number, boolean, lists, etc.... We can have a different type of object/value inside our list

# A. >> We can have a list of strings ["a", "b", "c"] and assign it to a variable like the following :-

letters = ["a", "b", "c"]
print(letters)
# output:
# ['a', 'b', 'c']

names = ["Adam", "Billy", "Jane"]
print(names)
# output:
# ["Adam", "Billy", "Jane"]

# B. >> Also we can have a list of numbers of type integer or float, you can make a list of integers like the following :-

numbers = [1, 2, 3, 4, 5]
print(numbers)
# output:
# [1, 2, 3, 4, 5]

mix_of_numbers = [1, 2.3, 22, 23.2, 234]
print(mix_of_numbers)
# output:
# [1, 2.3, 22, 23.2, 234]

prices = [2.00, 3.99, 23.9, 12.40]
print(prices)
# output:
# [2.0, 3.99, 23.9, 12.4]

# C. >> We can have a list of lists, which means each item in a list will be a list itself as the following :-

matrix_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(matrix_list)
# output:
# [[1, 2], [3, 4], [5, 6], [7, 8]]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example define 50 items with value of 0 :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

list_of_zeros = [0] * 50
print(list_of_zeros)
# output:
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example concatenate multiple lists :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

letters = ["a", "b", "c"]
zeros = [0] * 5

combined = letters + zeros
print(combined)
# output:
# ['a', 'b', 'c', 0, 0, 0, 0, 0]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example combine two list of names :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

company_a = ['Adam', "Sally"]
company_b = ['John', "Frank", "David"]

new_company = company_a + company_b
print(new_company)
# output:
# ['Adam', 'Sally', 'John', 'Frank', 'David']

# endregion

################################################################
################ Using the list() Functions  ###################
################################################################
# region
print("#" * 50)

# The list() function is a build-in function used to convert an iterated object into a list

characters = list("Hello World")
print(characters)
# output:
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Create a list of numbers from 1 to 20 - Using the range method :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = list(range(1, 21))

print(numbers)
# output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# endregion

################################################################
############ Using the len() Functions with list ###############
################################################################
# region

# We use the len function to get the length of out list

numbers = [1, 2, 5, 3, 64, 32]
print(len(numbers))
# output: 6

characters = ['a', 'b', 'c']
print(len(characters))
# output: 3

name = ["Adam", "William", "Frank", "John", "David"]
print(len(name))
# output: 5

# endregion

################################################################
################ Access List/2DList Items with indexing ########
################################################################
# region
print("#" * 50)

# To access individual item in our list, we use square brackets [], and specify the item index position
# out index always start at 0 for the first item in the list
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#   0    1    2    3    4    5    6
#  -7   -6   -5   -4   -3   -2   -1

# A. >> Get the first item from a list

letters = ['a', 'b', 'c', 'd']
print(letters[0])
# output:
# a

# B. >> Get different items from list , by specifying different index position

letters = ['a', 'b', 'c', 'd']
print(letters[0])  # output: a
print(letters[1])  # output: b
print(letters[2])  # output: c
print(letters[3])  # output: d
# print(letters[5]) # output: >>>> IndexError: list index out of range

# >> C. Get last item from a list, by specifying an index position of -1, which will return the first item from rhe end of the list

letters = ['adam', 'frank', 'william', 'david']
print(letters[-1])

# >> D. Access 2D List

matrix_list = [[1, 2], [3, 4], [5, 6], [7, 8]]

print(matrix_list[0][0])  # output: 1
print(matrix_list[0][1])  # output: 2
print(matrix_list[2][1])  # output: 6
print(matrix_list[3][0])  # output: 7

# Using for-in loop to iterate thru 2D List

for row in matrix_list:
    for item in row:
        print(item)

# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

# endregion

################################################################
######### Access/Return multiple Items from a List [:] #########
################################################################
# region
print("#" * 50)

# Just like string we specify the start and end index :-
# [:] --> return the list itself
# [<start_index_include>:] --> start at index and include then return after till the end
# [:<end_index_not_include>] --> end at index and not include then return before till the start
# [<start_index_include>:<end_index_not_include>] --> start at index and include and stop at end index but don't include
# [<start_index_include>:<end_index_not_include>:<step_jump_count>] --> step count mean how many element to skip

# >> A. Return the original list without modifying it

letters = ['adam', 'frank', 'william', 'david']
print(letters[:])
# output: ['adam', 'frank', 'william', 'david']

# >> B. Specify the start index with include with print everything after it - [<start_index_include>:]

letters = ['adam', 'frank', 'william', 'david']
print(letters[0:])
# start at 0 index include then print everything after it
# output: ['adam', 'frank', 'william', 'david']

letters = ['adam', 'frank', 'william', 'david']
print(letters[2:])
# start at 2 index include then print everything after it
# output: ['william', 'david']

letters = ['adam', 'frank', 'william', 'david']
print(letters[3:])
# start at 3 index include then print everything after it
# output: ['david']

letters = ['adam', 'frank', 'william', 'david']
print(letters[-2:])
# start at -2 index include then print everything after it
# output: ['william', 'david']

letters = ['adam', 'frank', 'william', 'david']
print(letters[-4:])
# start at -4 index include then print everything after it
# output: ['adam', 'frank', 'william', 'david']


# >> C. Specify the end index without including it ten print everything before it till the start - [<start_index_include>:]

letters = ['adam', 'frank', 'william', 'david']
# start at index 2 without including it, then print every thing before it
print(letters[:2])
# output: ['adam', 'frank']

letters = ['adam', 'frank', 'william', 'david']
# start at index 3 without including it, then print every thing before it
print(letters[:3])
# output: ['adam', 'frank', 'william']

letters = ['adam', 'frank', 'william', 'david']
# start at index 4 without including it, then print every thing before it
print(letters[:4])
# output: ['adam', 'frank', 'william', 'david']

letters = ['adam', 'frank', 'william', 'david']
# start at index 0 without including it, then print every thing before it
print(letters[:0])
# output: []

letters = ['adam', 'frank', 'william', 'david']
# start at index 1 without including it, then print every thing before it
print(letters[:1])
# output: ['adam']

letters = ['adam', 'frank', 'william', 'david']
# start at index -1 without including it, then print every thing before it
print(letters[:-1])
# output: ['adam', 'frank', 'william']

letters = ['adam', 'frank', 'william', 'david']
# start at index -3 without including it, then print every thing before it
print(letters[:-3])
# output: ['adam']

# >> D. Specify the start index with including it, then end with index without including it - [<start_index_include>:<end_index_not_include>]

letters = ['adam', 'frank', 'william', 'david']
# start between at 0 index while including it till 2 index without including it
print(letters[0:2])
# output: ['adam', 'frank']

letters = ['adam', 'frank', 'william', 'david']
# start between at 1 index while including it till 4 index without including it
print(letters[1:4])
# output: ['frank', 'william', 'david']

letters = ['adam', 'frank', 'william', 'david']
# start between at 1 index while including it till 4 index without including it
print(letters[2:5])
# output: ['william', 'david']]

letters = ['adam', 'frank', 'william', 'david']
# start between at 1 index while including it till -1 index without including it
print(letters[0:-1])
# output: ['adam', 'frank', 'william']

letters = ['adam', 'frank', 'william', 'david']
# start between at 1 index while including it till -2 index without including it
print(letters[1:-2])
# output: ['frank']

# the following won't return anything, don't start with negative index
print(letters[-1:-2])  # output: [ ]
print(letters[-2:-3])  # output: []

# >> E. Specify the Skip count element - [<start_index_include>:<end_index_not_include>:<step_jump_count>]

letters = ['adam', 'frank', 'william', 'david']
# no skip
print(letters[::1])
# output: ['adam', 'frank', 'william', 'david']

letters = ['adam', 'frank', 'william', 'david']
# no skip
print(letters[::2])
# output: ['adam', 'william']

letters = ['adam', 'frank', 'william', 'david']
# no skip
print(letters[0:4:2])
# output: ['adam', 'william']

numbers = list(range(20))
print(numbers[::2])
# output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Reverse order
numbers = list(range(20))
print(numbers[::-1])
# output: [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# endregion

################################################################
############# Change/Update Item from the List #################
################################################################
# region
print("#" * 50)

# Modifying/changing items from a list by specifying the item index position then assign value to that item index.
# my_list[<item_index_position>] = "new_value"

# >> A. Update your list a character of items

letters = ['a', 'b', 'c', 'd']

letters[0] = "X"
print(letters)
# ['X', 'b', 'c', 'd']

letters[3] = "X"
print(letters)
# ['X', 'b', 'c', 'X']

# >> B. An Example

my_list = [1, 'two', 3, 4, 'five']
print(my_list)  # output: [1, 'two', 3, 4, 'five']
my_list[1] = 2
my_list[4] = 5
print(my_list)  # output: [1, 2, 3, 4, 5]

# >> C. An Example

names = ["John", "Bob", "David", "Sally"]
names[3] = "Frank"
names[0] = ""
print(names)
# output: ['', 'Bob', 'David', 'Frank']


# endregion

################################################################
########### Iterate thru a list using for-in Loop ##############
################################################################
# region
print("#" * 50)

# Looping thru/over lists, by using the for-in loop to loop over any list of items

# A. >> Iterate thru Items on a list using for-in loop

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4, 5]
names = ['Adam', "William", "Sally"]

for char in letters:
    print(char)

# output:
# a
# b
# c

for num in numbers:
    print(num)

# output:
# 1
# 2
# 3
# 4
# 5

for name in names:
    print(name)

# output:
# Adam
# William
# Sally

# B. >> to get the index of each item, we use a build in function called enumerate() that return tuples for each item (item_name, item_index)

letters = ['a', 'b', 'c']

for item in enumerate(letters):
    print(item)
    print("Item name:", item[0])
    print("Item index:", item[1])

# output:
# (0, 'a')
# Item name: 0
# Item index: a
# (1, 'b')
# Item name: 1
# Item index: b
# (2, 'c')
# Item name: 2
# Item index: c

# C. >> Using unpacking to get the index and name of each item, with enumerate() build-in function :-

# var1, var2 = [1,2]
# var1, var2 = (0,'a')

letters = ['a', 'b', 'c']

for index, letter in enumerate(letters):
    print(item)
    print("Item name:", index)
    print("Item index:", letter)

# output:
# (0, 'a')
# Item name: 0
# Item index: a
# (1, 'b')
# Item name: 1
# Item index: b
# (2, 'c')
# Item name: 2
# Item index: c

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - get the largest number from the list of numbers
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = [10, 3, 6, 2, 8, 4]

max = numbers[0]

for num in numbers:
    if max < num:
        max = num

print("The largest number is", max)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - increase every item on the list by +3
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = [1, 2, 3, 4, 5]
current_index = 0

for num in numbers:
    numbers[current_index] = num + 3
    current_index += 1

print(numbers)
# output: [4, 5, 6, 7, 8]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - increase every item on the list by +3 using enumerate build-in function
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = [1, 2, 3, 4, 5]

for index, num in enumerate(numbers):
    numbers[index] = num + 3

print(numbers)
# output: [4, 5, 6, 7, 8]

# endregion

################################################################
#################### Adding/Removing Items #####################
## append(), insert(), pop(), remove(), clear(), count(), del ##
################################################################
# region
print("#xx" * 50)

# We have a build-in functions that we can use to new items to a list or remove existing items.
# To add item into a list, you need to decide where to add this new item.
# If you want to add an Item at the end of the list use the append(obj) method
# If you want to add an Item at a specific position index use the insert(index, obj) method
# If you want to remove an Item at the end of the list or at specific index use the pop() or pop(index) method
# If you want to remove an Item by specifying the name use the remove(item_name) method
# If you want to remove an Item index position or remove a range of items use the del statement
# If you want to remove all items from the list use the clear() method


# A. >> append(item): Add items at the end of the list

letters = ['a', 'b', 'c']

letters.append("d")
print(letters)
# output: ['a', 'b', 'c', 'd']

letters.append("e")
letters.append("f")
letters.append("g")
print(letters)
# output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters.append(22)
letters.append(12)
print(letters)
# output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 22, 12]

# >>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>

items = [
    ("product_1", 10),
    ("product_1", 9),
    ("product_1", 12)
]

prices = []

for item in items:
    prices.append(item)

print(prices)
# output:
# [10, 9, 12]

# B. >> insert(index, item): Add items at a specific position index

letters = ['b', 'c', 'd']
# add at the beginning of the list
letters.insert(0, "a")
print(letters)
# output: ['a', 'b', 'c', 'd']
letters.insert(1, "bb")
print(letters)
# output: ['a', 'bb', 'b', 'c', 'd']
letters.insert(-1, "z")
print(letters)
# output: ['a', 'bb', 'b', 'c', 'z', 'd']
letters.insert(3, "cc")
print(letters)
# output: ['a', 'bb', 'b', 'cc', 'c', 'z', 'd']
letters.insert(7, "zz")
print(letters)
# output: ['a', 'bb', 'b', 'cc', 'c', 'z', 'd', 'zz']

# C. >> pop(): Remove an item at the end of the list

names = ["Adam", "William", "John", "Sally"]
names.pop()
print(names)
# output: ['Adam', 'William', 'John']
names.pop()
names.pop()
print(names)
# output: ['Adam']

# D. >> pop(index): Remove an item at a specific index

letters = ['a', 'b', 'c', 'd', 'e', 'z']
letters.pop(0)  # remove first item from the list
print(letters)
# output: ['b', 'c', 'd', 'e', 'z']
letters.pop(2)
print(letters)
# output: ['b', 'c', 'e', 'z']
letters.pop(-1)  # remove last item from the list
print(letters)
# output: ['b', 'c', 'e']

# E. >> remove(item_name): Remove an item by its name, only remove the first occurring of the value

letters = ['a', 'b', 'c', 'd', 'e', 'z', 'b', 'c']
letters.remove("a")
print(letters)
# output: ['b', 'c', 'd', 'e', 'z', 'b', 'c']
letters.remove("b")
print(letters)
# output: ['c', 'd', 'e', 'z', 'b', 'c']
letters.remove("c")
letters.remove("d")
print(letters)
# output: ['e', 'z', 'b', 'c']

# E. >> del statement: Remove an item by index or delete a range of items

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

del letters[0]
print(letters)
# output: ['b', 'c', 'd', 'e', 'f', 'g']
del letters[2]
print(letters)
# output: ['b', 'c', 'e', 'f', 'g']
del letters[1:4]
print(letters)
# output: ['b', 'g']

# F. >> clear(): to remove all items from the list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters.clear()
print(letters)
# output: []

# endregion

################################################################
#################### Finding/Count/Sorting #####################
######### index(), count(), sort(), reverse() sorted(list)  ####
################################################################
# region
print("#Y" * 50)

# We have a build-in method that give us the index of a given item/object in a list called index(item_name):int method
# If you want to return number of occurrences of value use the count(item_name):int method
# We can sort out any list we use the sort() method

# A. >> Find an item index using the index(item_name):int method

letters = ['a', 'b', 'c']

print(letters.index("a"))  # output: 0
print(letters.index("b"))  # output: 1
print(letters.index("c"))  # output: 2
# print(letters.index("e")) # output: ValueError: 'e' is not in list

if "e" in letters:
    print(letters.index("e"))

# B. >> count(): to return number of occurrences of value.

letters = ['a', 'b', 'c', 'c', 'e', 'a', 'a']
print(letters.count('a'))  # output: 3
print(letters.count('b'))  # output: 1
print(letters.count('c'))  # output: 2

# C. >> copy(): to copy list into a new variable without effecting it with the original list

numbers = [5, 3, 4, 6, 7, 8]

copied_numbers = numbers.copy()
numbers.append(200)

print(copied_numbers)
# output:
# [5, 3, 4, 6, 7, 8]

print(numbers)
# output:
# [5, 3, 4, 6, 7, 8, 200]

# D. >> list.sort(): to sort list in ascending order lower to higher

numbers = [3, 51, 2, 8, 6, 44]
numbers.sort()
print(numbers)
# output:
# [2, 3, 6, 8, 44, 51]

names = ["Frank", "William", "David", "Adam"]

names.sort()
print(names)
# output: ['Adam', 'David', 'Frank', 'William']

# E. >> list.sort(reverse=True): to sort list in descending order higher to lower

numbers = [3, 51, 2, 8, 6, 44]
numbers.sort(reverse=True)
print(numbers)
# output:
# [51, 44, 8, 6, 3, 2]

# F. >> list.reverse(): to sort list in descending order higher to lower

numbers = [3, 51, 2, 8, 6, 44]
numbers.reverse()
print(numbers)
# output:
# [51, 44, 8, 6, 3, 2]

# G. >> sorted(Iterable, reverse=True):list to sort list in ascending order lower to higher, sorted method won't modify the original list

numbers = [3, 51, 2, 8, 6, 44]

print(sorted(numbers))
# output: [2, 3, 6, 8, 44, 51]
print(numbers)
# output: [3, 51, 2, 8, 6, 44]
print(sorted(numbers, reverse=True))
# output: [51, 44, 8, 6, 3, 2]

# H. >> sort a list of tuples

items = [
    ("Product_2", 30),
    ("Product_1", 20),
    ("Product_3", 10)
]


def sort_item(item):
    return item[1]  # get the price or number of the item


# sort by key number
items.sort(key=sort_item)

# or use lambda expression
items.sort(key=lambda item: item[1])

print(items)
# output: [('Product_3', 10), ('Product_1', 20), ('Product_2', 30)]

# endregion

################################################################
#### List Unpacking var1, var2, var3,.. and using *var_name ####
################################################################
# region

# A. >> To get individual items from lists/tuples and assign them to different variables like the following

numbers = [1, 2, 3]
var1 = numbers[0]
var2 = numbers[1]
var3 = numbers[2]
print(var1, var2, var3)
# output:
# 1 2 3

# B. >> Instead you can use List unpacking, which is elegant and readable, we can unpack a list into multiple variables within the same line.

numbers = [1, 2, 3]

# unpack the list of numbers into the variables on the left side of the assignment operator
var1, var2, var3 = numbers

print(var1, var2, var3)
# output:
# 1 2 3

# C. >> You will get an error if you don't unpack all list element into variables like the following

numbers = [1, 2, 3]

# var1, var2 = numbers
# ValueError: too many values to unpack (expected 2)
# mean not enough variable provided

# D. >> Unpack a few items without worry about the rest, like only define three variable for the first three item and store the rest into other variable as a list again

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#  *<variable_name> will packing the rest of the items from the list and store them as list again
var1, var2, var3, *other = numbers

print(var1, var2, var3)
# output: 1 2 3

print(other)
# output: [4, 5, 6, 7, 8, 9]

# E. >> Unpack the first and last item from the list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first, *other, last = numbers

print(first, last)
# output: 1 9

print(other)
# output: [2, 3, 4, 5, 6, 7, 8]

# endregion

################################################################
############# List - Map(), Filter(), zip() Method #############
################################################################
# region
print("############## List - Map(), Filter() and zip() Methods ##############")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> A. map() method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# The map method is used to Iterator thru a list and each item on that list is passed into a method
# map() method returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# >> Using the map() Method :-
# map(func, iterable)

my_list = [1, 2, 3, 4, 5]


def Multiply_by_2(item):
    return item * 2


new_list = map(Multiply_by_2, my_list)

print(new_list)
# output: <map object at 0x000001BB5649BE80>
print(list(new_list))
# output: [2, 4, 6, 8, 10]

# >> B. Using lambda expression

new_list = map(lambda num: num * 2, my_list)

print(list(new_list))
# output: [2, 4, 6, 8, 10]

# >>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example
# >>>>>>>>>>>>>>>>>>>>>>>>>

items = [
    ("product_1", 10),
    ("product_2", 9),
    ("product_3", 12)
]

price = []

result = map(lambda item: item[1], items)

for item in result:
    print(item)

# output:
# 10
# 9
# 12

print(list(result))
# output:
# [10, 9, 12]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> B. filter() method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# the filter method runs iterable into a function and return either true or false
# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# it return an iteration yield

numbers = [2, 5, 21, 51, 3, 6, 12]


def filter_list(num):
    return num > 20


new_numbers = filter(filter_list, numbers)

print(list(new_numbers))
# output:
# [21, 51]

# >> Using lambda expression
new_numbers = filter(lambda num: num > 20, numbers)

for item in new_numbers:
    print(item)

# output:
# 21
# 51

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>

items = [
    ("product_1", 10),
    ("product_2", 9),
    ("product_3", 12)
]

result = filter(lambda item: item[1] >= 10, items)

print(result)
# output:
# <filter object at 0x000001A720BA2AA0>

for item in result:
    print(item)

# output:
# ('product_1', 10)
# ('product_3', 12)

# >>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example :-
# >>>>>>>>>>>>>>>>>>>>>>>>


def check_even(num):
    return num % 2 == 0


list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

result = filter(check_even, list_of_nums)

for num in result:
    print(num)

# output:
# 2
# 4
# 6
# 8
# 10
# 12

print(list(filter(check_even, list_of_nums)))
# output:
# [2, 4, 6, 8, 10, 12]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> C. zip() method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 1. what is the zip method :-
# it zip lists together, it returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.

# 2. zip syntax :-
# zip(iterator1, iterator2, iterator3 ...)

list1 = [1, 2, 3]
list2 = [10, 20, 30]

result = zip(list1, list2)

print(list(result))
# output:
# [(1, 10), (2, 20), (3, 30)]

print(list(zip('abc', list1, list2)))
# output:
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

# >>>>>>>>>>>>
# Example 1
# >>>>>>>>>>>>

myList1 = [1, 2, 3]
myList2 = ['a', 'b', 'c']

myZip = zip(myList1, myList2)

print(myZip)
# output: <zip object at 0x0000026773182840>

print(tuple(myZip))
# output: ((1, 'a'), (2, 'b'), (3, 'c'))

for item in zip(myList1, myList2):
    print(item)

# output:
# (1, 'a')
# (2, 'b')
# (3, 'c')

# If your list not even or not the same length, like the following :-
myList1 = [1, 2, 3, 4, 5]
myList2 = ['a', 'b', 'c']

print(list(zip(myList1, myList2)))
# output: [(1, 'a'), (2, 'b'), (3, 'c')]

# As you see above, it will ignore the remaining

# >>>>>>>>>>
# Example 2
# >>>>>>>>>>>

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(x)
# output: <zip object at 0x000002177E952AC0>

# Use the tuple() function to display a readable version of the result:

print(tuple(x))
# output:
# (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 3 - convert zip tuples into a list
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result))
# output: [('Java', 14), ('Python', 3), ('JavaScript', 6)]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 4 - convert zip tuples into a list
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

myList1 = [1, 2, 3]
myList2 = ['a', 'b', 'c']
myList3 = [100, 200, 300]

result = zip(myList1, myList2, myList3)
print(list(result))
# output: [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

# endregion

################################################################
##################### List Comprehensions ######################
################################################################
# region

# List Comprehensions allow us to build our lists using a different notation.
# By adding for-in loop inside a bracket with an element result capture at the beginning
# three for loop will append element output into an element holder

# List Comprehensions Syntax :-

# result = [<expression> for <Item> in <Items>]
# The for-in loop is used to iterate over iteration and then applying this <expression> on each item
# [Item for <Item> in <Items>]
# above we store each item into Item expression

# Instead of using the following :-

my_string = "hello"
my_list = []

for letter in my_string:
    my_list.append(letter)

    # We can use the following below :-

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 1 - Grab every letter in string
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >> here we store each letter into letter variable expression
my_char_list = [letter for letter in "word"]

print(my_char_list)
# output:
# ['w', 'o', 'r', 'd']

# print(letter)
# NameError: name 'num' is not defined.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 2 - map items using list Comprehensions  -
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

items = [
    ("product_1", 10),
    ("product_2", 9),
    ("product_3", 12)
]

result = list(map(lambda item: item[1], items))
# similar to :-
result = [item[1] for item in items]

print(result)
# output:
# [10, 9, 12]

for item in result:
    print(item)

# output:
# 10
# 9
# 12

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 3 - filter items using list Comprehensions  -
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

items = [
    ("product_1", 10),
    ("product_2", 9),
    ("product_3", 12)
]

result = list(filter(lambda item: item[1] >= 1, items))
# similar to :-
result = [item for item in items if item[1] >= 10]

print(result)
# output:
# [('product_1', 10), ('product_3', 12)]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 4 - Grab every number from range
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_num_list = [num for num in range(1, 11)]

print(my_num_list)
# output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Example 5 - Square numbers in range and turn into list
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_num_list = [num*2 for num in range(1, 11)]

print(my_num_list)
# output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# similar to :-

my_num_list = []

for num in range(1, 11):
    my_num_list.append(num * 2)

print(my_num_list)
# output:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# endregion

################################################################
################# Using the 'in' operator ######################
################################################################
# region

# We use the in operator to check if our value does exist in our list.

numbers = [4, 3, 2, 6, 8, 7]

print(3 in numbers)
# output: True

print(20 in numbers)
# output: False

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> An Example - Remove a duplicate from a list
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

my_list = [2, 2, 4, 6, 2, 4, 6, 1]
uniques = []

for num in my_list:
    if num not in uniques:
        uniques.append(num)

print("Unique numbers are:", uniques)
# output:
# Unique numbers are: [2, 4, 6, 1]

# endregion
