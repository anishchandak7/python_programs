
n, k, q = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
a = a[-k:] + a[:-k]
for _ in range(q):
    print(a[int(input())])