# cook your dish here
for _ in range(int(input())):
    x,a,b=map(int,input().split())
    r=a+((100-x)*b)
    print(r*10)
