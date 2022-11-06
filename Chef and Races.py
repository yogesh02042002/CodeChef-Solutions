# cook your dish here
for i in range(int(input())):
    X,Y,A,B = map(int, input().split())
    if X!= A and X!= B and Y!=A and Y!=B:
        print(2)
    elif (X==A or X==B) and (Y==A or Y==B):
        print(0)
    else:
        print(1)
