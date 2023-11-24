#9. Write a function that take a string and return number of words in it.
def num_of_words(string) :
    words = string.split()
    return len(words)
string = input("Enter a string : ")
print("Number of Words in a String is :", num_of_words(string))