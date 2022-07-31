a = int(input())
a_1 = set(map(int, input().split()))

n = int(input())

for i in range(n):
    
    comm, ne = input().split()
    b = set(map(int, input().split()))

    if comm == 'intersection_update':
        a_1.intersection_update(b)

    elif comm == 'update':
        a_1.update(b)

    elif comm == 'difference_update':
        a_1.difference_update(b)

    elif comm == 'symmetric_difference_update':
        a_1.symmetric_difference_update(b)
    
print(sum(a_1))
