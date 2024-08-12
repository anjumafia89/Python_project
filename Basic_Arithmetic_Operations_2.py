#Create a program that calculates the area and perimeter of a rectangle. Take the length and width as input from the user.

length=float(input('Enter a number: '))
width=float(input('Enter a number: '))
area = length * width
perimeter = 2 * (length + width)
print('The area of rectengle: ',area)
print('The perimeter of rectengle: ',perimeter)