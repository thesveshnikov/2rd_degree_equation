import math

# VALUES
a = float(input("Enter the value of A:\n"))
b = float(input("Enter the value of B:\n"))
c = float(input("Enter the value of C:\n"))

# DELTA
delta = b ** 2 - 4 * a * c

# ROOTS
if delta < 0:
    print("It has no real roots.")
elif delta == 0:
    root = -b / (2 * a)
    print(f"It has one real root: {root:.2f}")
else:
    sqrt_delta = math.sqrt(delta)
    root_1 = (-b + sqrt_delta) / (2 * a)
    root_2 = (-b - sqrt_delta) / (2 * a)
    print(f"The roots are: {root_1:.2f} and {root_2:.2f}")
