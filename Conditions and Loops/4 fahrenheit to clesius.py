# Read input as sepcified in the question
# Print output as specified in the question
S = int(input())
E = int(input())
W = int(input())

while S<=E:
    print(S,int((S-32)*5/9))
    
    S = S + W
    
