# cook your dish here
for _ in range(int(input())):
    d,n=map(int,input().split())
    sum=0
    while(d>0):
        sum=0
        for i in range(n+1):
            sum=sum+i
        n=sum
        d=d-1
    print(sum)
    
