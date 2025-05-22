import math
from fractions import Fraction

# VALUES
a = float(input("Enter the value of A:\n"))
b = float(input("Enter the value of B:\n"))
c = float(input("Enter the value of C:\n"))

# CONVERTING TO FRACTION
a_frac = Fraction(a).limit_denominator()
b_frac = Fraction(b).limit_denominator()
c_frac = Fraction(c).limit_denominator()

# DELTA
delta = b ** 2 - 4 * a * c

# ROOTS
if delta < 0:
    print("It has no real roots.")
elif delta == 0:
    root = -b / (2 * a)
    root_frac = Fraction(root).limit_denominator()
    if root.is_integer():
        print(f"It has one real root: {int(root)}")
    else:
        print(f"It has one real root: {root_frac}")
else:
    sqrt_delta = math.sqrt(delta)
    root_1 = (-b + sqrt_delta) / (2 * a)
    root_2 = (-b - sqrt_delta) / (2 * a)
    
    root_1_frac = Fraction(root_1).limit_denominator()
    root_2_frac = Fraction(root_2).limit_denominator()
    
    def format_root(root, root_frac):
        if root.is_integer():
            return str(int(root))
        else:
            return str(root_frac)
    
    root_1_str = format_root(root_1, root_1_frac)
    root_2_str = format_root(root_2, root_2_frac)
    
    print(f"The roots are: {root_1_str} and {root_2_str}")
