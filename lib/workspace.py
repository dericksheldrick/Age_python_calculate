# Simple program that calculate the current age 
# the users enter the year of birth and we give them the age 

# def date_of_birth(year):
#     current_year = 2025
#     age = current_year - year
#     print(f'You are {age} years old!')

#     return age

# date_of_birth(1987)


# year_of_birth =[2000,1994,2005,1985,2010]

# def yearCalculate(year_of_birth):
#         for year in year_of_birth:
#                 current_date =2025
#                 age = current_date - year
#                 print(age)

# yearCalculate(year_of_birth)

# --------------------------------------------------------------------------------
# rearranging elements in order using list.sort()

# my_list = [3,6,7,2,1,4,9,5]
# my_list.sort()
# print(my_list)

# my_food = ["Cabbage","Banana", "Apple", "Orange"]
# my_food.sort()
# print(my_food) #reange it in alphanumeric order#

# my_lists = ['This is a long sentence', 'Word', 'z']
# my_lists.sort(key=len) #sort it from smallest to larget
# print(my_lists)
# my_lists.sort(key= len, reverse=True)
# print(my_lists) #from the largest to the smallest

# my_report= [('John', 2), ('Steve', 1), ('Anne', 3)]
# def sort_tuple(tuple_value):
#         return tuple_value[0]#Arrange using values , to rearrange them 

# my_report.sort(key= sort_tuple)
# print(my_report)

# ------------------------------------------------------------------------------------

# Sorted() returns the sorted copy of the original list
# used mostly when you need to main the integrity of the original copyright
# but you need ordered list for a different task

# my_list = [3, 6, 4, 2, 1, 5]
# sorted_list = sorted(my_list)
# print(my_list) #Original list 
# print(sorted_list)# sorted on 

# my_words = ['Loquacious', 'Chatty', 'Talkative']
# sorted_word = sorted(my_words, key=len, reverse=True)# can still use this with sorted()
# print(sorted_word)

# -------------------------------------------------------------------------------------------------

# Adding and removing from a list 
# list.append() => addeds the element at the end
# list.insert() => it takes two arg, the index and a value.if the value is available at the selected index,
#                  it is added and the everything moves by 1. 
#                  If no value exists at the index, the new value is added to the end of the existing list

# del() removes elements from a list, specified by an index or range of indices.
# list.pop() removes and returns the element at the index passed in as an argument. 
#          When used without any arguments, it removes and returns the last element of the list.
# list.remove() removes the element passed in as an argument. This is one of the few list methods that searches by value instead of index!

# list.clear() erases all of the values of a list. This is usually not a very useful tool, 
#         but it's a fast way to free up memory on your device if you're working with a particularly large list in the Python shell.

# ----------------------------------------------------------------------------------------------------------------------------------------


# Codewar => vowel remover
# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
#    Exaample 
#         "hello"     -->  "hll"
#         "codewars"  -->  "cdwrs"
#         "goodbye"   -->  "gdby"
#         "HELLO"     -->  "HELLO"
# Pseucode 
# 1.def the function that takes the string as a parameter
# 2.loop through the string 
# 3.check whether there is vowel letters o the characters 
# 4.remove the character 
# 5.return the remaining letters
