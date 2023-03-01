## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())
i=0
n1=0
n2=1
n3=0
while i<N:
    n1=n2
    n2=n3
    n3=n1+n2
    i=i+1
print(n3)