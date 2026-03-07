#  wap to calculate simple interest and validate result
# Program to calculate simple interest and validate input

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

# Validation
if p > 0 and r > 0 and t > 0:
    si = (p * r * t) / 100
    print("Simple Interest =", si)
else:
    print("Invalid input! Principal, Rate and Time must be greater than 0.")