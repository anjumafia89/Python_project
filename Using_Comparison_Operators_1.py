#Write a program that takes two numbers and checks if they are equal, not equal, greater than, less than, greater than or equal to, and less than or equal.

x=int(input('Enter a number: '))
y=int(input('Enter a number: '))
if x==y:
    print('Equal')
else:
    print('Not Equal')
if x>y:
    print('x is greater than y')
else:
    print('x is not greater than y')
if x<y:
    print('x is less than y')
else:
    print('x is not less than y')
if x>=y:
    print('x is greater than y or equal')
else:
    print('x is not greater than y or equal')
if x<=y:
    print('x is less than y or equal')
else:
    print('x is not less than y or equal')
