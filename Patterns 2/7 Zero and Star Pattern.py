'''
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    stars=1
    while stars<=i:
        if stars==i:
            print('*',end='')
            stars+=1
        else:
            print('0',end='')
            stars+=1
    zeros=z2=1
    while zeros<=n-i:
        print('0',end='')
        zeros+=1
    print('*',end='')
    
    r=1
    while r<=n-i+1:
        if r==n-i+1:
            print('*',end='')
            r+=1
        else:
            print('0',end='')
            r+=1
    while z2<=i-1:
        print('0',end='')
        z2+=1
    print()
    i=i+1
        