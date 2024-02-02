# def convert_zone(x,y,zone):
#     if zone==0: return x,y
#     if zone==1: return y,x
#     if zone==2: return -y,x
#     if zone==3: return -x,y
#     if zone==4: return -x,-y
#     if zone==5: return -y,-x
#     if zone==6: return y,-x
#     if zone==7: return x,-y

def midPointCircleAlgorithm(radius):
    # Initial d
    d = 1 - radius
    x = 0
    y = radius

    pixels_in_zone = []

    while x < y:
        # x_p, y_p = convert_zone(x, y, zone)
        d_info = f"x: {x}, y: {y}, d: {d}" # Updated_Pixel: ({x_p}, {y_p})"
        pixels_in_zone.append(d_info)
        
        if d < 0:
            # IF EAST
            d += 2*x + 3
            x += 1
        else:
            # IF SOUTH
            d += 2*x - 2*y + 5
            x += 1
            y -= 1

    # x_p, y_p = convert_zone(x2, y2, zone)
    # d_info = f"x: {x2}, y: {y2}, d: {d}, Final Pixel: ({x_p}, {y_p})"
    # pixels_in_zone.append(d_info)

    return pixels_in_zone


r = int(input("Radius: "))
# desired_zone = int(input("Desired Zone (0-7): "))

# x_p, y_p = convert_zone(0,r,desired_zone)

resultant_pixels = midPointCircleAlgorithm(r)

for info in resultant_pixels:
    print(info)