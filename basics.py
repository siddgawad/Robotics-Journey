import math

x=3 
y=4.5

name="Sid"
nums=[1,2,3]
pose=(1.0,2.0,0.5)

robot = {
    "name":"turtlebot3",
    "wheel_radius":0.033,
    "base_width":0.16
}

print("x+y=", x+y)
print("robot name:", robot["name"])
print("first name:", nums[0])

angles_deg = [0, 30, 45, 90]

for angle in angles_deg:
    rad = angle*math.pi / 180.0
    print(angle, "deg=", rad, "rad")


