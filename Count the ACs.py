# cook your dish here
for _ in range(int(input())):
    p=int(input())
    r=(p//100)+(p%100)
    if r<=10:
        print(r)
    else:
        print("-1")
