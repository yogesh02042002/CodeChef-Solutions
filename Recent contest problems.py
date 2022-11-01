for _ in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    sum=0
    count=0
    for i in l:
        if i=="START38":
            count=count+1
        else:
            sum=sum+1
    print(count,sum)
        
