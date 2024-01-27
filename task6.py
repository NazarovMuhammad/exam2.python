a = input().split()
a[0],a[len(a)] = a[len(a)],a[0]
print(a)