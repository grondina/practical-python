# mortgage.py
#
# Exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_start = 61
extra_end = 108
extra_payment = 1000.0

fmt = '{:3d}' + ' {:>12.2f}'*3

while principal > 0:
    month += 1
    monthly_payment = payment
    if month >= extra_start and month <= extra_end:
        monthly_payment += extra_payment
    principal = principal * (1 + rate/12) - monthly_payment
    if principal < 0:
        monthly_payment -= abs(principal)
        principal = 0
    total_paid += monthly_payment
    print(fmt.format(month, monthly_payment, total_paid, principal))

print('Total paid', round(total_paid, 2))
print('Total months', month)

