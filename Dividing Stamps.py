# cook your dish here
n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(n):
    s += a[i]
if s == n*(n+1)/2:
    print('YES')
else:
    print('NO')
