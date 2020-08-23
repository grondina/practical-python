# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid += payment
    print('{:3d} {:>12.2f} {:>12.2f}'.format(month, total_paid, principal))

print('Total paid', round(total_paid, 2))

