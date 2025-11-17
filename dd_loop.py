import amth 
from robot_coords_min import world_to_robot

def step_dd(pose,v,w,dt):
    x,y,th = pose
    x += v* math.cos(th)*dt
    y += v* math.sin(th)*dt
    th += w* dt
    th = (th + math.pi) % (2*math.pi) - math.pi
    return (x,y,th)

def go_to_goal(goal_w,pose,kv=0.8,kw=3.0,v_max=0.6,w_max=2.0):
    xr, yr = world_to_robot(pose,goal_w)
    dist = math.hypot(xr,yr)
    head = math.atan2(yr,xr)
    