# cook your dish here
for _ in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a<b:
        if (b-a)<=x:
            print("YES")
        else:
            print("NO")
    elif a>b:
        if (a-b)<=y:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    
    
    
