#Create a program that takes three side lengths and determines if they can form a triangle.Additionally, check if the triangle is equilateral, isosceles, or scalene.

x=int(input('Enter a number'))
y=int(input('Enter a number'))
z=int(input('Enter a number'))

if x+y<=z or x+z<=y or y+z<=x:
    print('Not a triangle')
elif x==y==z:
    print(Equilateral)
elif x==y or x==z or y==z:
    print('Isosceles')
else:
    print('Scalene')