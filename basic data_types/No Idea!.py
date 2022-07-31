a=input().split(' ')
b=([int(i) for i in input().split(' ')])
firstset=set([int(i) for i in input().split(' ')])
secondset=set([int(i) for i in input().split(' ')])
k=0
for i in b:
    if i in firstset:
        k+=1
    if i in secondset:
        k-=1
print(k)