#!/usr/bin/python3

l1 = [int(a) for a in input().split()]
l2 = [int(b) for b in input().split()]

res = [(a, b) for a in l1 for b in l2]

for i in res:
    print(i, end=" ")
print()
