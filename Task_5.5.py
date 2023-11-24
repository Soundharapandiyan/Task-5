# 5. Write a function that takes astring that returns True if it is palindrome else return False 
def palindrome(string) :
    j = len(string) -1
    for i in range(len(string)//2):
        if string[i].lower() == string[j].lower() :
            j -=1
        else :
            return False
    return True
string = input("Enter the string : ")


if palindrome(string) :
    print("Given string [",string,"] is palindrome")
else:
    print("Given string [",string,"] is not palindrome")