# cook your dish here
for _ in range(int(input())):
    m,h=map(int,input().split())
    r=m/(h**2)
    if r<=18:
        print("1")
    elif r<=24:
        print("2")
    elif r<=29:
        print("3")
    else:
        print("4")
