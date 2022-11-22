# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    t=b-a
    if t%3==0 or t%3==1:
        print("YES")
    else:
        print("NO")
