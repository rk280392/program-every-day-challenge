#/usr/bin/python3

from itertools import product

l1 = [int(a) for a in input().split()]
l2 = [int(b) for b in input().split()]


for pair in list(product(l1,l2)):
    print(pair, end=" ")
print()
