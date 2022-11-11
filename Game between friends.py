# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if a<b:
        a=a+c
    else:
        b=b+c
    if b>a:
        a=a+d
    else:
        b=b+d
        
    if a<b   : 
        print("S")
    else:
        print("N")
