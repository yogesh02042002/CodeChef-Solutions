# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if sum(a) == 5:
        print("Jeff Dean")
    elif sum(a) == 4:
        print("Hacker")
    elif sum(a) == 3:
        print("Senior Developer")
    elif sum(a) == 2:
        print("Middle Developer")
    elif sum(a) == 1:
        print("Junior Developer")
    else:
        print("Beginner")
        
        
