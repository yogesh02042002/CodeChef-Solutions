# cook your dish here
for _ in range(int(input())):
    n,x = map(int, input().split())
    if n==1:
        print(x)
    elif n%6==0:
        print(n//6*x)
    else:
        print((n//6)*x+x)
        
