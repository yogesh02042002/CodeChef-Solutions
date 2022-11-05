# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=list(input())
    l=''
    for i in s:
        if i == "A":
            l+="T"
        elif i == "G":
            l+="C"
        elif i == "T":
            l+="A"
        elif i == "C":
            l+="G"
    print(l)
