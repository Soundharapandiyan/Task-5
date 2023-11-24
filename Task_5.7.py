#7. Write a function that takes a string a return the most frequent character in the string.
def most_freq_char (str1):
    char_dict = {}
    for i in str1 :
        if i not in char_dict :
            char_dict[i] = 1
        else :
            char_dict[i] += 1
    most_frequent_char =[]
    max_count = 0
    for char,count in char_dict.items() :
         if max_count < count :
             max_count = count
    for char,count in char_dict.items():
        if count == max_count :
            most_frequent_char.append(char)
    return most_frequent_char
str1 = input("Enter the string : ")
print(" ".join(most_freq_char(str1)))