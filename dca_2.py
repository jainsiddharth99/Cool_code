a= int(input())
b=[]
for i in range(9,1,-1):
    while a%i==0:
        # print(i)
        a=a/i
        # print(i)
        b.append(i)
b.reverse()
# str1=[str(i) for i in b]
# str2="".join(str1)

# print(int(str2)
for i in b:
    print(i,end="")