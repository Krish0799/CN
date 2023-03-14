'''
Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
12345
1234
123
12
1
'''

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
k=n
while i<=n:
    j=1
    while j<=k:
        print(j,end='')
        j=j+1
    print()
    k=k-1
    i=i+1