#Develop a program that takes three numbers as input and prints the largest and smallest of the three numbers.

n1 = int(input('Enter a number: '))
n2 = int(input('Enter a number: '))
n3 = int(input('Enter a number: '))

largest = n1
smallest = n1

# for largest
if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3

# for smallest
if n2 < smallest:
    smallest = n2
if n3 < smallest:
    smallest = n3
print(f'Largest number: {largest} and Smallest number: {smallest} ')
