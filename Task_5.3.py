# 3. write a function that takes a string and return all the vowels removed

def str_re_vowel():
    string = input("Enter the string: ")
    vowels = "AaEeIiOoUu"
    new_string = ""
    
    for char in string:
        if char not in vowels:
            new_string += char
    
    return new_string

print(str_re_vowel())