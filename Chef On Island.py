# cook your dish here
for _ in range(int(input())):
    x,y,Xr,Yr,d=map(int,input().split())
    if min((x/Xr),(y/Yr))>=d:
        print("YES")
    else:
        print("NO")
