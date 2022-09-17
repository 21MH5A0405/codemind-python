n=int(input())
t=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
c=(t**2)
d=(rev**2)
e=len(str(c))
f=len(str(d))
if e==f:
    print('True')
else:
    print('False')