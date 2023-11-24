# #4. write a function that takes a string and returns number of  unique characters in it.

def no_of_uni_char (input):
    unique_chars = set()
    for char in input:
        unique_chars.add(char)
    return len(unique_chars)
input =input("Enter the string : ")
unique_count = no_of_uni_char(input)
print("Number of unique characters:", unique_count)