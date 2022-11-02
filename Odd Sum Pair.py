for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)%2!=0 or (a+c)%2!=0 or (b+c)%2!=0:
        print("yes")
    else:
        print("no")
