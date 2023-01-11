# cook your dish here
for _ in range(int(input())):
    c = 0
    n = int(input())
    a = input()
    for i in range(n - 1):
        if a[i] == a[i+1]:
            c+=1
    print(c)
