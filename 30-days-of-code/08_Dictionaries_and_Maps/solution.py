import sys
n=int(input())
phone_book = dict(input().split() for _ in range(n))
    
for i in range(n):
    name = input()
    if name in phone_book:
        print("{0}={1}".format(name, phone_book[name]))
    else:
        print("Not found")