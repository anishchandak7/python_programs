import statistics
n = int(input())
arr = list(map(int,input().split()))
mean = statistics.mean(arr)
median = statistics.median(arr)
#mode = statistics.mode(arr)
def most_element(liste):
    numeral=[[liste.count(nb), nb] for nb in liste]
    numeral.sort(key=lambda x:x[0], reverse=True)
    return(numeral[0][1])
print("%.1f"% mean)
print("%.1f"% median)
print("%.1f"%most_element(arr))