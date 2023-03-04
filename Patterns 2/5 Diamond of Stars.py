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
i=k=1
while i<=n:
    j=1
    spaces=1
    if i%2!=0:
        while spaces<=(n-i)/2:
            print(' ',end='')
            spaces=spaces+1
    if i%2!=0:
        while j<=i:
            print('*',end='')
            j=j+1
        print()
    i=i+1
while k<=n-2:
    if k%2!=0:
        spaces_=1
        while spaces_<=k-spaces_+1:
            print(' ',end='')
            spaces_+=1
    j1=1
    if k%2!=0:
        p=k-1
        while j1<=n-2-p:
            print('*',end='')
            j1=j1+1
        print()
    k=k+1