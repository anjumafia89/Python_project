#Triangle Type Checker
#Develop a program that takes three side lengths and determines if they form a valid triangle. Additionally, check if the triangle is acute, obtuse, or right-angled.
a=int(input('First side length: '))
b=int(input('Second side length: '))
c=int(input('Third side length: '))

if a + b > c and b + c > a and c + a > b:
    print('Valid triangle')

    if a**2 + b**2 > c**2:
        print('Acute triangle')
    elif a**2 + b**2 < c**2:
        print('Obtuse triangle')
    elif a**2 + b**2 == c**2:
        print('Right-angled triangle')
else:
    print('Not a valid triangle')