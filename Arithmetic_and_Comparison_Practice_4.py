#Temperature Converter and Comparator: Write a program that converts temperatures between Celsius and Fahrenheit and compares if two temperatures are the same in different units.
c=float(input('Enter Celsius degree:'))
f=float(input('Enter fahrenheit degree:'))
#convert celsius to fahrenheit
fahrenheit=(c * 1.8) + 32
celsius = (f - 32) * 5/9
print('convert celsius to fahrenheit: ',fahrenheit)
print('convert fahrenheit to celsius: ',celsius)
if fahrenheit == f or celsius == c:
    print('Two temperatures are the same in different units.')
else:
    print('Two temperatures are not the same in different units.')