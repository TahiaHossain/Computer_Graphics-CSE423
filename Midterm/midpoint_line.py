def find_zone(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        if   dx>=0 and dy>=0: zone=0
        elif dx>=0 and dy<=0: zone=7
        elif dx<=0 and dy>=0: zone=3
        elif dx<=0 and dy<=0: zone=4
    else :
        if   dx>=0 and dy>=0: zone=1
        elif dx<=0 and dy>=0: zone=2
        elif dx<=0 and dy<=0: zone=5
        elif dx>=0 and dy<=0: zone=6
    return zone

def convert_to_zone_0(x,y,zone):
    if zone==0: return x,y
    if zone==1: return y,x
    if zone==2: return y,-x
    if zone==3: return -x,y
    if zone==4: return -x,-y
    if zone==5: return -y,-x
    if zone==6: return -y,x
    if zone==7: return x,-y
   
def convertOrigin(x,y,zone):
    if zone==0: return x,y
    if zone==1: return y,x
    if zone==2: return -y,x
    if zone==3: return -x,y
    if zone==4: return -x,-y
    if zone==5: return -y,-x
    if zone==6: return y,-x
    if zone==7: return x,-y

def midpoint_line(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1

    d = (2*dy)-dx
    d_E = 2*dy
    d_NE = 2*(dy-dx)

# initializing points
    x = x1 
    y = y1

    pixels_on_line = []

    while (x<x2):
        x_p, y_p = convertOrigin(x, y, zone)
        d_info = f"x: {x}, y: {y}, d: {d}, Updated_Pixel: ({x_p}, {y_p})"
        pixels_on_line.append(d_info)

        if d < 0 :
            # d_up = 'E'
            x += 1
            d += d_E
        else :
            # d_up = "NE"
            x += 1
            y += 1
            d += d_NE

    # Append the endpoint
    x_p, y_p = convertOrigin(x2, y2, zone)
    d_info = f"x: {x2}, y: {y2}, d: {d}, Final Pixel: ({x_p}, {y_p})"
    pixels_on_line.append(d_info)

    return pixels_on_line

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

current_zone = find_zone(x1, y1, x2, y2)
x1_prime, y1_prime = convert_to_zone_0(x1, y1, current_zone)
x2_prime, y2_prime = convert_to_zone_0(x2, y2, current_zone)

pixels_on_line = midpoint_line(x1_prime, y1_prime, x2_prime, y2_prime, current_zone)

print("Current Zone: ", current_zone)

for info in pixels_on_line:
    print(info)