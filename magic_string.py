'''Eva has a string S containing lowercase English letters. She wants to transform this 
string into a Magic String, where all the characters in the string are the same. To do 
so, she can replace any letter in the string with another letter present in that string. 6
Your task is to help Eva find and return an integer value, representing the minimum 
number of steps required to form a Magic String. Return 0, if S is already a Magic 
String.
Input Specification:
input1: A string S, containing lowercase English letters.
Output Specification:
Return an integer value, representing the minimum number of steps required to form 
a Magic String. Return 0, if S is already a Magic String.
Sample Input:
aaabbbccdddd
Sample Output:
8
'''


def magic_string(str1):
 a=0
 max1=0
 b=len(str1)
 for ele in str1:
    a=str1.count(ele)
    if a==b:
        return 0
    elif a>max1:
        max1=a
 return b-max1      
str1=input()        
print(magic_string(str1))
