for _ in range(int(input())):

    n,k=map(int,input().split())

    x=(k*(k+1))//2

    if n>=x:

        print("YES")

    else:

        print("NO")
