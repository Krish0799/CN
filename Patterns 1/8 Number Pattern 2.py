## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if i==2 or i==1:
            print('1',end='')
        else:
            if j==i or j==1:
                print(i-1,end='')
            else:
                print('0',end='')
        j=j+1
    print()
    i=i+1