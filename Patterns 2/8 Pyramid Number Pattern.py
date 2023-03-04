'''
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
       212
      32123
     4321234
    543212345

'''
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    right=2
    left=2
    sp=1
    sp2=1
    while sp<=n-i:
        print(' ',end='')
        sp+=1
    endv=i
    while right<=i:
        print(endv,end='')
        endv-=1
        right+=1
    print(1,end='')
    while left<=i:
        print(left,end='')
        left+=1
    print()
    i=i+1
        