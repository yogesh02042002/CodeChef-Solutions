# cook your dish here
for _ in range(int(input())):
    n,l,x=map(int,input().split())
    r = n-l
    print(min(r,l)*x)
    
        
