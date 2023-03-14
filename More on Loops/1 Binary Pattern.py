'''
Print the following pattern for the given number of rows.
Pattern for N = 4
1111
000
11
0
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
11111
0000
111
00
1
'''

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
k=1
for i in range(n,i-1,-1):

    if k%2!=0:
        for one in range(1,i+1):
            print(1,end='')
    else:
        for zero in range(1,i+1):
            print(0,end='')
    k=k+1
    print()
#n=int(input())
#i=1
#k=1
#for i in range(n+1):
#    for x in range(i,n+1):
#        if k%2!=0:
#            print(1,end='')
#        else:
#            print(0,end='')
#    k=k+1
#    print()