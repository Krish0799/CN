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