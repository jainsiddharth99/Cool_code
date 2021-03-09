X=int(input())
a=[]
if X>=1 and X<=10:
    for i in range(X):
        val=int(input())
        if val>=1 and val<=1000:
            a.append(val)
n=int(input())
a.sort()
if n>=1 and n<=X:
    print(a[n-1])