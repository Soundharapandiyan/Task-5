# 1. Write a python program to calculate total number of vowels and count of each individual vowels A,E,I,O,U in the string "Guvi Geeks Network Private limited"
vowels = ["A", "E", "I", "O", "U"] 
string = "Guvi Geeks Network Private limited"
string = string.upper()
total_number_of_vowels = 0
vowel_dictionary = {}
for char in string:
    if char in vowels:
        total_number_of_vowels += 1
        if char not in vowel_dictionary:
            vowel_dictionary[char] = 1
        else:
            vowel_dictionary[char] += 1

print("Total number of vowels:", total_number_of_vowels)
print("Vowel count:")
for vowel, count in vowel_dictionary.items():
    print(vowel, ":", count)