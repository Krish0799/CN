'''
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *
'''
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
spaces=int(n/2)
for i in range(1,n+1):
    if i%2!=0:
        s=1
        for s in range(spaces):
            print(' ',end='')
        spaces-=1
        for stars in range(i):
            print('*',end='')
        print()
for j in range(n+1):
    k=int(j/2)
    if j%2!=0:
        for s in range(k+1):
            print(' ',end='')
        for stars in range(n-j-1):
            print('*',end='')
        print()
    k=k+1