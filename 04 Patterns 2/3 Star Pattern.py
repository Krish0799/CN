'''Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******
 '''



## Read input as specified in the question.
## Print output as specified in the question.

n=int(input())
i=1
while i<=n:
    spaces = 1
    while spaces<=n-i:
        print(' ',end='')
        spaces=spaces+1
    star = 1
    while star<=i:
        if star==1:
            print('*',end='')
        else:
            print('*',end='*')
        star=star+1
    print()
    i=i+1