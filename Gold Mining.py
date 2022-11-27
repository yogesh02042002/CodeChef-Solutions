# cook your dish here
for _ in range(int(input())):
    n,x,y=map(int,input().split())
    if (n+1)*y>=x:
        print("yes")
    else:
        print("no")
