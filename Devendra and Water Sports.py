# cook your dish here
for _ in range(int(input())):
    z,y,a,b,c=map(int,input().split())
    r=z-y
    if (a+b+c)<=r:
        print("YES")
    else:
        print("NO")
