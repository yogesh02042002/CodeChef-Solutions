# cook your dish here
for _ in range(int(input())):
    a,x,b,y = map(int,input().split())
    c= a/x 
    d= b/y
    if c==d:
        print("equal")
    elif c>d:
        print("Alice")
    else:
        print("Bob")
