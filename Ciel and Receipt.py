# cook your dish here
# cook your dish here
a=[1,2,4,8,16,32,64,128,256,512,1024,2048]
for i in range(int(input())):
    p=int(input())
    m=0
    for j in range(12,0,-1):
        m=m+p//(2**(j-1))
        p%=2**(j-1)
    print(m)
