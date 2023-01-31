# cook your dish here
import math
for t in range(int(input())):
    x,y=map(int,input().split())
    a=math.ceil(x/10)
    b=math.ceil(y/10)
    print(abs(a-b))
