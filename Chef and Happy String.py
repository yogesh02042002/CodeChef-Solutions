# cook your dish here
v={"a","e","i","o","u"}
for _ in range(int(input())):
    s=input()
    c=0
    lst=[]
    for i in range(len(s)):
        if s[i] in v:
            c+=1
        else:
            lst.append(c)
            c=0
    lst.append(c)
    if max(lst)>2:
        print("Happy")
    else:
        print("Sad")
