x_min = int(input("x_min: "))
y_min = int(input("y_min: "))
x_max = int(input("x_max: "))
y_max = int(input("x_max: "))

x0 = int(input("x0: "))
y0 = int(input("y0: "))
x1 = int(input("x1: "))
y1 = int(input("y1: "))

print()

line_vector_d = (x1-x0, y1-y0)
print("Line Vector, D: ", line_vector_d)

t_left = (x_min-x0) / (x1-x0)
t_right = (x_max-x0) / (x1-x0)
t_top = (y_max-y0) / (y1-y0)
t_bottom = (y_min-y0) / (y1-y0)

print("t_left: ", t_left)
print("t_right: ", t_right)
print("t_top: ", t_top)
print("t_bottom: ", t_bottom)