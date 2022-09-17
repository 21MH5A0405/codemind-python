n=int(input())
m=int(input())
for i in range(n,m+1):
    s=str(i) #10
    l=len(s) #2
    c=0
    for j in s:
        if int(j)!=0:
            
            if i%int(j)==0:
                c+=1
    if c==l:
        print(i,end=' ')