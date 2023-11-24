#  6. Write a function that takes two strings and returns the longest common substring between them. 
def longest_substring(str_1,str_2) :
    long_common_str = ""
    for i in range(len(str_1)) :
        for j in range(len(str_2)) :
            common_str = ""
            k = 0
            while i + k < len(str_1) and j +k < len(str_2) and str_1[i+k] == str_2[j+k] :
                common_str += str_1[i+k]
                k += 1
            if len(common_str) > len(long_common_str) :
                long_common_str = common_str
    return long_common_str      
str_1 = input(" Enter string 1 : ")
str_2 = input(" Enter string 2 : ")
print("longest common substring is : ", longest_substring(str_1,str_2))    