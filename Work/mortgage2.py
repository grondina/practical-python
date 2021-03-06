# mortgage.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_begin = 1
extra_end = 12
extra_payment = 1000.0

while principal > 0:
    month += 1
    monthly_payment = payment
    if month >= extra_begin and month <= extra_end:
        monthly_payment += extra_payment
    principal = principal * (1 + rate/12) - monthly_payment
    total_paid += monthly_payment
    print('{:3d} {:>12.2f} {:>12.2f}'.format(month, total_paid, principal))

print('Total paid', round(total_paid, 2))
print('Total months', month)

