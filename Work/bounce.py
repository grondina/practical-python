# bounce.py
#
# Exercise 1.5

height = 100 # meters
factor = 3/5
bounce = 0

while bounce < 10:
    height *= factor
    bounce += 1
    print(bounce, round(height, 4))

