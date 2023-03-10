
'''
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Input format :
N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26
Sample Input 1:
8
Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH
Sample Input 2:
7
Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG
'''
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while n>=1:
    j=1
    st=chr(ord('A')+n-1)
    while j<=i:
        strv=chr(ord(st)+j-1)
        print(strv,end='')
        j=j+1
    print()
    i=i+1
    n=n-1