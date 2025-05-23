import math
from fractions import Fraction

def solve_incomplete(a, b, c):
    if b == 0:
        if a == 0:
            return "Not a quadratic equation."
        if c == 0:
            return [0]
        if (-c/a) < 0:
            return "It has no real roots."
        root = math.sqrt(-c / a)
        root_frac = Fraction(root).limit_denominator()
        roots = [root, -root]
        return roots
    
    elif c == 0:
        if a == 0:
            return [0]
        roots = [0, -b/a]
        return roots
    
    return None

def format_root(root):
    root_frac = Fraction(root).limit_denominator()
    if root.is_integer():
        return str(int(root))
    else:
        return str(root_frac)

# VALUES
a = float(input("Enter the value of A:\n"))
b = float(input("Enter the value of B:\n"))
c = float(input("Enter the value of C:\n"))

# CONVERTING TO FRACTION
a_frac = Fraction(a).limit_denominator()
b_frac = Fraction(b).limit_denominator()
c_frac = Fraction(c).limit_denominator()

incomplete_roots = solve_incomplete(a, b, c)

if incomplete_roots is not None:
    if isinstance(incomplete_roots, str):
        print(incomplete_roots)
    else:
        formatted_roots = [format_root(root) for root in incomplete_roots]
        if len(formatted_roots) == 1:
            print(f"It has one real root: {formatted_roots[0]}")
        else:
            print(f"The roots are: {formatted_roots[0]} and {formatted_roots[1]}")
else:
    delta = b ** 2 - 4 * a * c

    # ROOTS
    if delta < 0:
        print("It has no real roots.")
    elif delta == 0:
        root = -b / (2 * a)
        root_str = format_root(root)
        print(f"It has one real root: {root_str}")
    else:
        sqrt_delta = math.sqrt(delta)
        root_1 = (-b + sqrt_delta) / (2 * a)
        root_2 = (-b - sqrt_delta) / (2 * a)
        
        root_1_str = format_root(root_1)
        root_2_str = format_root(root_2)
        
        print(f"The roots are: {root_1_str} and {root_2_str}")
