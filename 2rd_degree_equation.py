# VALUES
a = input("Enter the value of A:\n")
b = input("Enter the value of B:\n")
c = input("Enter the value of C:\n")

# DELTA
delta = int(b)*int(b)-int(4)*int(a)*int(c)

# ROOTS
if delta < 0:
    print("It has no real roots.")

if delta > 0:
    positive_b = abs(int(b))
    root_1 = (positive_b+delta)/(2*int(a))
    root_2 = (positive_b-delta)/(2*int(a))
    print("The roots are: ", root_1, "And", root_2)
