1. Frame is a point (origin) + 2 perpendicular axes in (2d) or 3 (in 3d), it defines how you measure posiiton and direction 
2. It is a point in space exists independently of any frame, and coordinates are just the numbers of that same point as expressed in one frame.
3. So the same physical point can ahve different coordinate values in:  a. the world frame, b. robot frame c. dpeending on where each frame is
Now deending on where each frame is- the transform between frames in 2d (robot to world) is:
T = [cos(theta) -sin(theta) x; sin(theta) cos(theta) y; 0 0 1];

where (x,y) = where the robot origin sits in the world frame and theta is robot's heading angle relative to the world x-axis

So to convert robot fram coordinate to world frame - 
1. Make it homogeneous: Pr = [xr, yr, 1]^T
2. Multiply: Pw = T* Pr;
3. World coordinatres are the first two entries of Pw 

Now- to get world coordibnates of a robot-frame poiunt we rotate byt theta and add (x,y)

let us say robot pose in world is x,y,theta and robot frame poiunt is xr,yr 

Rotate by θ:

𝑥' = cos𝜃⋅𝑥𝑟−sin𝜃⋅𝑦𝑟

y' = sin𝜃⋅𝑥𝑟+cos𝜃⋅𝑦𝑟

then translate by x,y

xw= x'+x = cos𝜃⋅𝑥𝑟−sin𝜃⋅𝑦𝑟+x
yw = sin𝜃⋅𝑥𝑟+cos𝜃⋅𝑦𝑟+y