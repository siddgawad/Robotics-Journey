import math

def deg_to_rad(deg):
    return deg*math.pi/180.0

def hypotenuse(a,b):
    return math.sqrt(a*a + b*b)

def describe_robot(name, wheel_radius, base_width):
    print(f"Robot {name}: wheel={wheel_radius}, base={base_width}")

def distance_2d(p1,p2):
    """

    p1,p2 are (x,y) tuples
    Return eucledian distance
    """

    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx*dx + dy*dy)

if __name__ == "__main__":
    print("deg_to_rad(90):", deg_to_rad(90))
    print("hypotenuse(3,4):", hypotenuse(3,4))
    describe_robot("turtlebot3", 0.033, 0.16)
    print("distance_2d((0,0),(3,4)):", distance_2d((0,0),(3,4)))


