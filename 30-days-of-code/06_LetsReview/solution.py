for i in range(int(input())):
    
    n = str(input().strip()).split()
    lst= list(n)
#[list(i) for i in lst if i %2 ==0]
    for i in lst:
        l = list(i)
    #print("{0} {1}".format(*l[::2], *l[::3]))
        print(*["".join(l[::2]),"".join(l[1::2])])
