def checkPalindrome(num):
    res=0
    t=num
    while num!=0:
        v=num%10
        res=res*10+v
        num=int(num/10)
    if t==res:
        return True
    else:
        return False

		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
