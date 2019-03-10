n = int(input())
arr = list(map(int, input().split()))
max_value = max(arr)
while(True):
    if max_value in arr:
        arr.remove(max_value)
    if max_value not in arr:
        break

print(max(arr))