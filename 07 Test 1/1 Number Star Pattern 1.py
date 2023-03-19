'''
Print the following pattern for given number of rows.
Input format :
Integer N (Total number of rows)
Output Format :
Pattern in N lines
Sample Input :
   5
Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321
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
n_c=n
while i<=n:
    j=1
    while j<=n:
        if j==n_c:
            print('*',end='')
        elif j!=n_c:
            print(n-j+1,end='')
        j=j+1
    n_c=n_c-1
    print()
    i=i+1