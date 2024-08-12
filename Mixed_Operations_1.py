#Simple Interest Calculator
# Write a program that calculates the simple interest given the principal, rate of interest, and time. Then, check if the interest is above a certain amount.

principal=int(input('Enter principle amount'))
rate_of_interest=int(input('Enter rate of interest %'))
time=int(input('Enter time'))

simple_interest=(principal*rate_of_interest*time)/100
print('The simple inerest will be: ',simple_interest)

certain_amount=int(input('Enter certain amount'))
if simple_interest>certain_amount:
    print('The interest is above the certain amount')
else:
    print('The interest is not above the certain amount')