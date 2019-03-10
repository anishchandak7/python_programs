import math
n = int(input())
x = list(map(int,input().split()))


def mean(x, n):
    sum1 = 0
    counter = 0
    while (counter < n):
        sum1 = sum1 + x[counter]
        counter += 1

    mean = sum1 / n
    return mean



mean1 = mean(x,n)
sum2 = 0
for value in x:
    sum2 = sum2+(value-mean1)**2

sd = math.sqrt(sum2/n)
print("%.1f"%sd)


