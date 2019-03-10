import math

counter = int(input("Number="))
position_list=[]
for i in range(counter):
    position_list.append(int(input()))

a_numbers = set()
p = 0
while True:
    p += 1
    test_q = p * p + 1
    k_found = False
    for k in range(1, int(math.sqrt(test_q)) + 1):
        if not test_q % k:
            q = -(p + k)
            r = -((p ** 2 + 1) // k + p)
            if q > r:
                a_numbers.add(p * q * r)
    #            print(p,q,r)

    if len(a_numbers) >= counter * 3:
        break

ass = sorted(list(a_numbers))
for i in range(counter):
    index = position_list[i]-1
    print(ass[index])

