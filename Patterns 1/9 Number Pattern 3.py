## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if i==1 or j==1 or j==i:
            print('1',end='')
        else:
            print('2',end='')
        j=j+1
    print()
    i=i+1