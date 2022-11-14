import math
for _ in range(int(input())):
    b,l=map(int,input().split())
    n=l**2-b**2
    m=b**2+l**2
    print(round(math.sqrt(n),5), round(math.sqrt(m),5))
