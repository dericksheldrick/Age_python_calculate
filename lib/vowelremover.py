#pseudocode

# 1.define a function called shortcut that takes a string as a parameter
# 2.declare a variable that contain the vowels.
# 3.loop through the string to check for the vowels.
# 5.chck if each letter in the string is vowel and remove it
# 6.declare an new_str variable that will contain non_vowel str.
# 7. assign non_vowel characters to the new_str variabe 
# 8. return the new_str variable

# Example
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"

def shortcut(string):
    vowel = "aeiou"
    new_str= ""
    for char in string:
        if char not in vowel:
            new_str += char
    return new_str

print(shortcut("hello"))
print(shortcut("codewars"))
print(shortcut("goodbye"))
print(shortcut("HELLO"))


 
# 