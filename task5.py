a = input().split()
maxi = a.index(max(a))
mini =  a.index(min(a))
a[mini],a[maxi]=a[maxi],a[mini]
print(a)
