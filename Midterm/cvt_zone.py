def convert_zone(x,y,zone):
    if zone==0: return x,y
    if zone==1: return y,x
    if zone==2: return -y,x
    if zone==3: return -x,y
    if zone==4: return -x,-y
    if zone==5: return -y,-x
    if zone==6: return y,-x
    if zone==7: return x,-y

x = int(input("x: "))
y = int(input("y: "))
zone = int(input("Required Zone: "))

result = convert_zone(x,y,zone)
print(result)