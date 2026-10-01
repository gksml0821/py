#깃허브 5번
'''a = list(map(int, input().split()))
print(max(a))
''' 

max_value=a[0]

for i in range(1,len(a)):
    if max_value < a[i]:
        max_value = a[i]
print(max_value)
