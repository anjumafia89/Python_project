#Develop a program that simulates a simple banking system.Take an initial balance and a series of transactions(deposits and withdrawals), then print the final balance.Ensure that withdrawals do not exceed the current balance.
i = float(input("Enter the initial balance: "))
d = float(input("Enter the deposit balance: "))
w = float(input("Enter the withdraw balance: "))

initial_balance = i

if d > 0:
    initial_balance = initial_balance + d
    print('After deposit ', initial_balance)

if w <= initial_balance:
    initial_balance = initial_balance - w
    print('After withdrawal:', initial_balance)
else:
    print("Insufficient balance for this withdrawal.")