'''You work in the message encoding department of a national security agency. Every message 
that is sent from or received in your office is encoded. You have an integer N, and each digit 
of N is squared and the squares are concatenated together to encode the original number. 
Your task is to find and return an integer value representing the encoded value of the 
number.
input1: An integer value N representing the number to be encoded.
Output :
Return an integer value representing the encoded value of the number.
Sample Input:
167
Sample Output:
13649
'''

num=int(input("Enter number"))
dig=str(num)
a=''
for ele in dig:
     res=str(int(ele)**2)
     a+=res
     g=int(a)
print(g)

