for i in range(int(input())):
    a,b,c=map(int,input().split())
    l=[b*j for j in range(a+1)]
    if c in l:
        print("YES")
    else:
        print("NO")
