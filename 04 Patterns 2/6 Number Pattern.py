'''
Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5

1        1
12      12
123    123
1234  4321
1234554321
'''
n=int(input())
i=1
e=n*2-2
printvalue=1
while i<=n:
    increment=1
    while increment<=i:
        print(increment,end='')
        increment+=1
    spaces=1
    
    while spaces<=e:
        print(' ',end='')
        spaces+=1
    e-=2
    rincrement=1
    printvalue=i
    while rincrement<=i:
        print(printvalue,end='')
        printvalue-=1
        rincrement+=1
    print()
    i=i+1