'''You are competing in a basketball contest. In this contest the score for each 
successful shot depends on both the distance from the basket and the player's 
position. The ball is shot N times, successfully. You are given an array A containing the 
distance of a player from basket for N shots. The index of array represents 
the position of the player. Score is calculated by multiplying the position with the 
distance from the basket.
Your task is to find and return an integer value, representing the maximum possible 
score you can achieve by choosing a contiguous subarray of size K from the given 
array.
Sample Input: 
n=6
K=3
A=[4,3,2,7,1,9]

Sample output:36
'''

n=int(input())
K=int(input())
A=list(map(int,input().split()))
maxx=0
for i in range(0,n-K+1):
    a=A[i:i+K]
    summ=0
    inc=1
    for j in a:
        summ=summ+(j*inc)
        inc+=1
    if summ>maxx:
        maxx=summ
print(maxx)
