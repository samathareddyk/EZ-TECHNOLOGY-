''' You are given a string containing words separated by spaces. Your task is to write a 
function or program that reverses the order of words in the string.
Sample Input:Hello World
Sample Output:World Hello
'''

str=input("Enter the words")
s=str.split()[::-1]
l=[]
for i in s:
    l.append(i)
print(" ".join(l))

