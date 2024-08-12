#Leap Year Checker
# Create a program that checks if a given year is a leap year or not.
year = int(input('Enter a year: '))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f'This {year} is leap year')
else:
    print(f'This {year} is not leap year')