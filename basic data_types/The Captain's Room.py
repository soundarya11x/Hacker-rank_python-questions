d=input()
a=input().split()
s1=set()
s2=set()  
for i in a:
    if  i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
print (list(s3)[0])
