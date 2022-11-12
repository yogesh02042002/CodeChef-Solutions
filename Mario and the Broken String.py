for _ in range(int(input())):
    n=int(input())
    s=input()
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:]
    if s1==s2:
        print("YES")
    else:
        print("NO")
