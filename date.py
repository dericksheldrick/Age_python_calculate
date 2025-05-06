# Simple program that calculate the current age 
# the users enter the year of birth and we give them the age 

def date_of_birth(year):
    current_year = 2025
    age = current_year - year
    print(f'You are {age} years old!')

    return age

date_of_birth(1987)