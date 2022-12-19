# cook your dish here

t = int(input())

for _ in range(t) :

    x,y,z = map(int,input().split())

    if y-x > 2*z :

        print("NO")

    else :

        print("YES")
