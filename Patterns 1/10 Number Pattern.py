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