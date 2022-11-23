# cook your dish here
for _ in range(int(input())):
    x1,x2,y1,y2=map(int,input().split())
    if (y1/x1)<(y2/x2):
        print("-1")
    elif (y1/x1)==(y2/x2):
        print("0")
    elif (y1/x1)>(y2/x2):
        print("1")
