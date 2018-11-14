# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:51:14 2018

@author: Anish
"""
#pattern 1
"""
54321
54321
54321
54321
54321
"""
"""
n = int(input())
for i in range(n):
    for j in range(n,0,-1):
        print(j,end="")
    print()
"""
#pattern 2
"""
55555
44444
33333
22222
11111
"""
"""
n = int(input())
count = n
for i in range(n):
    print(str(count)*n)
    count-=1
"""
#pattern 3
"""
12345
23456
34567
45678
56789
"""
"""
n = int(input())
count = n
for i in range(n):
    for j in range(i+1,count+1):
        print(j,end = "")
    print()
    count+=1
"""
#pattern 4
"""
98765
87654
76543
65432
54321
"""
"""
for k in range(4,-1,-1):
	for i in range (5,0,-1):
		print(k+i,end="")
	print()
"""
#pattern 5
"""
EEEEE
DDDDD
CCCCC
BBBBB
AAAAA
"""
"""
import string
list1 = list(string.ascii_uppercase)
a = input('enter the alphabet ')
a = a.upper()
index = list1.index(a)
temp = index
for i in range(index+1):
    print(list1[temp]*(index+1))
    temp-=1
"""
#pattern 6
"""
ABCDE
BCDEF
CDEFG
DEFGH
EFGHI
"""
"""
for k in range(65,70):
	for i in range (0,5):
		print(chr(k+i),end="")
	print()
"""
#pattern 7
"""
1*2*
1*2*
1*2*
1*2*
1*2*
"""
"""
for k in range(1,6):
	for i in range (1,3):
		print(f"{i}",end="*")
	print()
"""
#pattern 8
"""
10101
10101
10101
10101
10101
"""
"""
str1=""
n=int(input())
for i in range(n):
    if(i%2==0):
        k=1
    else:
        k=0
    str1 +=str(k)
    
for i in range(n):
    print(str1)
"""
#pattern 9
"""
1
21
321
4321
54321
"""
"""
n=int(input())
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
"""
#pattern 10
"""
1
23
345
4567
56789
"""
"""
n = int(input())
count = 0
l=2
for i in range(n):
    for j in range(i+1,count+l):
        print(j,end = "")
    print()
    count+=1
    l+=1
"""
#pattern 11
"""
1
32
543
7654
98765
"""
"""
n = int(input())
count = 0
l=2
for i in range(n):
    for j in range(count+l,i+1,-1):
        print(j-1,end = "")
    print()
    count+=1
    l+=1
"""
#pattern 12
"""
5
44
333
2222
11111
"""
"""
n=int(input())
t=1
for i in range(n,0,-1):
    print(str(i)*t,end="")
    print()
    t+=1
"""
#pattern 13
"""
5
45
345
2345
12345
"""
"""
c=5
for i in range(6):
    for j in range(1,i+1):
        print(c+j,end="")
    c-=1
    print()
"""
#pattern 14
"""
5
54
543
5432
54321
"""
"""
c=5 
for i in range(6):
    for j in range(i):
        print(c-j,end="")
    print()
"""
#pattern 15
"""
1
00
111
0000
11111
"""
"""
t=1
for i in range(5):
    if(i%2==0):
        print("1"*t,end="")
    else:
        print("0"*t,end="")
    t+=1
    print()
"""
#pattern 16
"""
1
10
101
1010
10101
"""
"""
for i in range(5):
    for j in range(i+1):
        if(j%2==0):
            print("1",end="")
        else:
            print("0",end="")
    print()
"""
#pattern 17
"""
1
01
010
1010
10101
"""
"""
x=1
for i in range(5):
    for j in range(i+1):
        print(x,end="")
        if(x==1):
            x=0
        else:
            x=1
    print()
"""
#pattern 18
"""
54321
4321
321
21
1
"""
"""
c=5
for i in range(5):
    t=c
    for j in range(5,i,-1):
        print(t,end="")
        t-=1
    c-=1
    print()
"""
#pattern 19
"""
12345
2345
345
45
5
"""
"""
c=1
for i in range(5):
    t=c
    for j in range(5,i,-1):
        print(t,end="")
        t+=1
    c+=1
    print()
"""
#pattern 20
"""
* * * * *
 * * * *
  * * * 
   * * 
    *
"""
"""
c=5
for i in range(5):
    print(" "*i+"* "*c,end=" ")
    c-=1
    print()
"""
#pattern 21
"""
5 4 3 2 1 
 4 3 2 1 
  3 2 1 
   2 1 
    1
"""
"""
wrong code
c=5
k=0
for i in range(5):
    for j in range(c,0,-1):
        print(" "*k+str(j),end=" ")
    c-=1
    k+=1
    print()
"""
