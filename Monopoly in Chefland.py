# cook your dish here
for _ in range(int(input())):
    R1,R2,R3=map(int,input().split())
    if R1+R2<R3 or R2+R3<R1 or R1+R3<R2:
        print("YES")
    else:
        print("NO")
