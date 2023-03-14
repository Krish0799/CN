'''
Print Number Pyramid
Send Feedback
Print the following pattern for a given n.
For eg. N = 6
123456
  23456
    3456
      456
        56
          6
        56
      456
    3456
  23456
123456
Sample Input 1 :
4
Sample Output 1 :
1234
  234
    34
      4
    34
  234
1234
'''
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n+1):
    for s in range(i-1):
        print(' ',end='')
    for d in range(i,n+1):
        print(d,end='')
    print()
k=n-1
for j in range(1,n):
    for sp in range(n-j-1):
        print(' ',end='')
    for inc in range(n-j,n+1,1):
        print(inc,end='')
        k-=1
    print()