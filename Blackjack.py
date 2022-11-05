# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=21-(a+b)
    if c in range(1,11):
        print(c)
    else:
        print('-1')
