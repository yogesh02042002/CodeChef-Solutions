# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if (2*x)>(5*y):
        print("Chocolate")
    elif (2*x)<(5*y):
        print("Candy")
    else:
        print("Either")
