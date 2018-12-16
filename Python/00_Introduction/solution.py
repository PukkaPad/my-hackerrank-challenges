# Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
if __name__ == '__main__':
    n = int(input())
    if n%2 == 0 and n in range(2,6):
        print ("Not Weird")
    
    elif n%2 == 0 and n in range(6, 21):
        print ("Weird")
    
    elif n%2 == 0 and n>20:
        print ("Not Weird")
        
    elif n%2 != 0:
        print ("Weird")


# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)


# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print("{0} \n{1}".format(round(a/b), (a/b)))
    

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Write a function
def is_leap(year):
    leap = False
    
    if year%4==0 and(year%100 !=0 or year%400==0):
        leap = True
                
                
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1), sep="")