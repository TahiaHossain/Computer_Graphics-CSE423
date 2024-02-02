def dda(x,y,m):
    x = x1
    y = y1

    pixels = []

    while (x < x2):

        d_info = f"x: {x}, y: {y}, Updated_Pixel: ({round(x)}, {round(y)})"
        pixels.append(d_info)

        if -1 <= m <= 1 :
            x += 1
            y += m
        else :
            x += (1/m)
            y += 1

    d_info = f"x: {x2}, y: {y2}, Final Pixel: ({x2}, {y2})"
    pixels.append(d_info)
    return pixels 

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

print()

m = (y2-y1) / (x2-x1)
print("m: ", m)
print("1/m: ", 1/m)

pixels_on_line = dda(x1,y1,m)

print()
for info in pixels_on_line :
    print(info)