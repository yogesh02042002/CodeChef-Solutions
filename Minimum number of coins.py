# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if x%10==0:
        print(x//10)
    elif x%5==0:
        print((x//10)+1)
    else:
        print(-1)
