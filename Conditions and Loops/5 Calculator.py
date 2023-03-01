# Write your code here
while 1:
    n = int(input())
    if n == 1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif n == 2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif n == 3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif n == 4:
        a = int(input())
        b = int(input())
        print(int(a/b))
    elif n == 5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif n == 6:
        break
    else:
        print("Invalid Operation")
    
        