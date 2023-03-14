'''
Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star.
Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
11
Sample Output :
*
 * *
   * * *
     * * * *
       * * * * *
         * * * * * *
       * * * * *
     * * * *
   * * *
 * *
*
'''

## Read input as specified in the question.
## Print output as specified in the question.
import math
n=int(input())
i=1
endvalue=math.ceil(n/2)
while i<=endvalue:
    spaces=2
    while spaces<=i:
        print(' ',end='')
        spaces+=1
    star=1
    no=1
    while star<=i:
        if star==i:
            while no<=i:
                print('*',end=' ')
                no+=1
            star+=1
        else:
            star+=1
    print()
    i+=1
k=1
while k<=endvalue:
    sp2=1
    while sp2<=endvalue-k-1:
        print(' ',end='')
        sp2+=1
    down=1
    while down<=endvalue-k:
        print('*',end=' ')
        down+=1
    print()
    k=k+1