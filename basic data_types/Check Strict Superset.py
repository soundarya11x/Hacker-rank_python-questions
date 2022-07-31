A,n = set(input().split()),int(input())
print(all([A.issuperset(set(input().split())) for i in range(n)]))
