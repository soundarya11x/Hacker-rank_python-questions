n1 = int(input())
a = set(input().split())

n2 = int(input())
b = set(input().split())

result = a.union(b) - a.intersection(b)
print(len(result))
