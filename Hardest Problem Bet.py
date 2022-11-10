for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if min(a,b,c)==c:
        print("Alice")
    elif min(a,b,c)==b:
        print("Bob")
    else:
        print("Draw")
