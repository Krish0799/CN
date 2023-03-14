'''
Print the following pattern for the given number of rows.
Pattern for N = 4
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
3
Sample Output :
33333
32223
32123
32223
33333
'''
## Read input as specified in the question.
## Print output as specified in the question.
import math
n=int(input())
k=n*2-1
p=n
for i in range(1,k+1):
    j=n
    ####
    if i>=n+1:
        e=i-n+1
    else:
        e=0
    d=n
    ####
    if i>=n+1:
        for d in range(d,e-1,-1):
            print(d,end='')
        for dc in range(i-n):
            print(i-n+1,end='')
        dl=1
        for dl in range(i-n-1):
           print(i-n+1,end='')
        dr=i-n+1
        for dr in range(i-n+1,n+1,1):
            print(dr,end='')
        print()
    else:
        for j in range(n,n-i,-1):
            print(j,end='')
        cvu=1
        for cvu in range(n-i-1):
            print(p,end='')
        for r in range(n-i):
            print(p,end='')
        if p==1:
            i=i-1
            p=p+1
        for ri in range(i):
            print(p+ri,end='')
        p-=1
        print()
   