# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sorted(a)
    k=[]
    for i in range(n-1):
        x=s[i+1]-s[i]
        k.append(x)
    print(min(100001,min(k) ))
