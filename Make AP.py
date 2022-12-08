# cook your dish here
for _ in range(int(input())):
    a,c=map(int,input().split())
    if ((a+c) % 2) != 0:
        print(int(-1))
    else: 
        print(int((a+c)/2))
