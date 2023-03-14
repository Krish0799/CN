'''
Print the following pattern for the given number of rows.
Pattern for N = 4



The dots represent spaces.



Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
         232
       34543
     4567654
   567898765
Sample Input 2:
4
Sample Output 2:
           1
         232
       34543
     4567654
'''

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
k=1 #@track of increment values
p=0 #@track of decrement values
#p is incremented 2 for each i itterations
#pv is decremented 1 for each j iterations
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    no=1
    k=i
    while no<=i:
        print(k,end='')
        no=no+1
        k=k+1
    j=1
    pv=p
    while j<=i-1:
        print(pv,end='')
        j=j+1
        pv-=1
    p=p+2
    print()
    i=i+1