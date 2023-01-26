# cook your dish here
n,h,x=map(int,input().split())
t=list(map(int,input().split()))
for i in t:
    if x+i>=h:
        print("YES")
        break
else:
    print("NO")
    
