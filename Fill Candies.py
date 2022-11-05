# cook your dish here
import math
for _ in range(int(input())):
    n,k,m=map(int,input().split())
    print(math.ceil(n/(k*m)))
