n=int(input())

power=pow(n,4)
# power=str(power)
# n=str(n)
# print(power[-1])
for i in power:
    if power[-1]==n:
        print('true')
    else:
        print('false')