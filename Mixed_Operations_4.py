#Quadratic Equation Solver
#Write a program that solves a quadratic equation and determines the nature of its roots (real and distinct, real and equal, or complex)

a=float(input('enter a coefficient number: '))
b=float(input('enter a coefficient number: '))
c=float(input('enter a coefficient number: '))

D=b**2-4*a*c
if D>0:
    print('The roots real and distinct')
if D==0:
    print('The roots real and equal')
else:
    print('The roots are complex(not real')