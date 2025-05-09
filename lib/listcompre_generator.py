# for x in range(1, 11):
#     result = x ** 2
#     print(result)

# List comprehension is here to simplify how we write the loops 
# and even run faster
# syntax:
#     new_list = [expression for item in iterable if conditions]

#example 1

# squared = [x **2 for x in range(1, 11)]
# even_squared = [x**2 for x in range(1, 11) if x % 2 == 0]
# #even_sqquared- has a condition at the end 
# print(squared)
# print(even_squared)

#example 2 - extracting the intials of my fruits name

fruits_name = ["mellon", "pineApple", "Apple", "Banana", "Oranges"]
vowel = "aeiou"
intials = [fruit[0] for fruit in fruits_name ]
lasts = [fruit[-1] for fruit in fruits_name if fruit[-1] == vowel ]

print(intials)
print(lasts)


