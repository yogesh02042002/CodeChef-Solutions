# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=list(input())
    l=""
    for i in range(0,n-1,2):
        if a[i]+a[i+1]=="00":
            l=l+"A"
        elif a[i]+a[i+1]=="01":
            l=l+"T"
        elif a[i]+a[i+1]=="10":
            l=l+"C"
        elif a[i]+a[i+1]=="11":
            l=l+"G"
    print(l)
