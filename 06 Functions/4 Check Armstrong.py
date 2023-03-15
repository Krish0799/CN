'''
Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
Input Format :
Integer n
Output Format :
true or false
Sample Input 1 :
1
Sample Output 1 :
true
Sample Input 2 :
103
Sample Output 2 :
false
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
def Amstrong(num):
    temp=num
    value=0
    while temp>0:
        r=temp%10
        cube=1
        for i in str(num):
            cube=cube*r
        value+=cube
        temp=temp//10
    if value==num:
        return True
    else:
        return False
    
num=int(input())

is_amstrong=Amstrong(num)

if is_amstrong:
    print('true')
else:
    print('false')