# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if (x+y)>z:
        print("TRAIN")
    elif(x+y)==z:
        print("EQUAL")
    else:
        print("PLANEBUS")
