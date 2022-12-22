# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n<4:
        print("MILD")
    elif n<7:
        print("MEDIUM")
    elif n>=7:
        print("HOT")
