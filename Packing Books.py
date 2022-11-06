# cook your dish here
import math
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print((math.ceil(y/z))*x)
