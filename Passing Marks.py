# cook your dish here
for _ in range(int(input())):
    a,b,c,T,A,B,C=map(int,input().split())
    t=(A+B+C)
    if A>=a and B>=b and C>=c and t>=T:
        print("YES")
    else:
        print("NO")
