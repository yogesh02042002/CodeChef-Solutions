# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    m=min(a,b,c)
    print((a+b+c)-m)
