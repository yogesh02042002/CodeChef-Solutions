for _ in range(int(input())):
    x=int(input())
    if x>65 and x<=100:
        print("Overload")
    elif x<35:
        print("Underload")
    else:
        print("Normal")
