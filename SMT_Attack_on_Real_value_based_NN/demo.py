from z3 import *
set_option(rational_to_decimal=True)
set_option(precision=2)
# Create real variables
x = Real('x')
y = Real('y')
k = Real('k')
i = BitVec('i' , 8)

a = 10
a = a >> 2
print(a)
# Create a solver
s = Solver()

# Add constraints to the solver
s.add(x == 1.21)
s.add(y == 3.42)
s.add(k == 1.21*3.42)
print(k)
#s.add(2*x - y == 1)

# Check if there is a satisfying solution
if s.check(x*y == 4.1382) == sat:
    # Get the model
    model = s.model()
    # Get the values of x and y from the model
    x_value = model[x].as_decimal(2) # Get the decimal representation with 2 decimal places
    y_value = model[y]  # Get the decimal representation with 2 decimal places
    k = model[k].as_decimal(2)
    

    print("Solution found:")
    print("x =", x_value)
    print("y =", y_value)
    print("k =" , k)
else:
    print("No solution found.")
