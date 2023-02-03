# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x<y and x<z:
        print("Alice")
    elif y<x and y<z:
        print("Bob")
    else:
        print("Charlie")
