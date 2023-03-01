#Write Your Code Here
N = int(input())
res = 0
while N != 0:
    V = N % 10	
    res = res * 10 + V
    N = int(N / 10)
print(res)
    