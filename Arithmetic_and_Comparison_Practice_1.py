#Average Calculator
#Write a program that takes three numbers as input and calculates their average. Then, check if the average is greater than a specified threshold.
x=int(input('Enter a number: '))
y=int(input('Enter a number: '))
z=int(input('Enter a number: '))

num=x+y+z
average=num/3
print('The average number will be: ',average)

threshold=int(input('Enter a threshold_value: '))

if average>threshold:
    print('The average is greater than a threshold.')
else:
    print('The average is not greater than a threshold.')