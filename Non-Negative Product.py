# cook your dish here
for i in range(int(input())):
    num=int(input())
    a=list(map(int,input().split()))
    x=1
    for i in range(num):
        x*=a[i]
    if(x<0):
        print(1)
    else:
        print(0)
