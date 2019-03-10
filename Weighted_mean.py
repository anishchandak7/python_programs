n = int(input())
x = list(map(int,input().split()))
w = list(map(int,input().split()))
sum1 = 0
counter = 0
while(counter<n):
    sum1 = sum1+x[counter]*w[counter]
    counter += 1

weighted_mean = sum1/sum(w)
print("%.1f"%weighted_mean)
