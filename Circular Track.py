# cook your dish here
for _ in range(int(input())):
    a,b,m=map(int,input().split())
    print(min(abs(a-b),abs(m-abs(a-b))))
