## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
N = int(input())
evn_sum=0
odd_sum=0
while N!=0:
    v=N%10
    if v%2==0:
        evn_sum+=v
    else:
        odd_sum+=v
    N=int(N/10)
print(evn_sum," ",odd_sum)