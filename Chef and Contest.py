# cook your dish here
for _ in range(int(input())):
    x,y,p,q=map(int,input().split())
    c=x+(p*10)
    ch=y+(q*10)
    if c>ch:
        print("Chefina")
    elif c<ch:
        print("Chef")
    else:
        print("Draw")
