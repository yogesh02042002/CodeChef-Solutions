# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if(a<=b and c<=b):
        print("YES")
    else:
        print("NO")
