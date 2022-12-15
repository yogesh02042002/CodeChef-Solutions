# cook your dish here
for _ in range(int(input())):
    a=int(input())
    if a <3:
        print("Light")
    elif a<7:
        print("Moderate")
    elif a>=7:
        print("Heavy")
    else:
        print("0")
