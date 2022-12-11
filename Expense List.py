# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    x=2**x 
    for j in range(n):
        x=x-(x*0.5)
    print(int(x))
