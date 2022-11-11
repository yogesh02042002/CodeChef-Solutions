# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=[]
    for i in l:
        count=l.count(i)
        s.append(count)
    x=max(s)
    print(n-x)
