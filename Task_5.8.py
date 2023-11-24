#8. Write a function that takes a string and return True if it is anagram with another string else return false.

def the_anagrams(str1, str2):
    str1 = str1.replace(" ", "").upper()
    str2 = str2.replace(" ", "").upper()
    return sorted(str1) == sorted(str2)
string1 = input("Enter a string : ")
string2 = input("Enter a string : ")
result = the_anagrams(string1, string2)
print(result)  