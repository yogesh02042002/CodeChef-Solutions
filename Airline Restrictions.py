for _ in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    if ((b+c)<=d and a<=e):
        print("yes")
    elif((a+c)<=d and b<=e):
        print("yes")
    elif((a+b)<=d and c<=e):
        print("yes")
    else:
        print("no")
