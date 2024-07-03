'''You have been given the task of making the content on a social media platform more 
user-friendly. Your task is to find and return an integer value representing the count 
of the number of spaces in a given string S.(Without using Built-in function)
Input:
A string S
Output :
Return an integer value representing the count of the number of spaces in a given 
string S.
Example:
Input:
Hello World Hey
Output:
2
'''


def check_space(str1):
 count=0
 for char in str1:
    if char==" ":
       count+=1
 return count 
str1=input()  
print(check_space(str1)) 

