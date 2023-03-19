'''
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
'''
from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        if j==i:
            print('*',end='')
        else:
            print(0,end='')
        j=j+1
    #center *
    print('*',end='')
    k=1
    while k<=n:
        if k==n-i+1:
            print('*',end='')
        else:
            print('0',end='')
        k=k+1
    print()
    i=i+1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    