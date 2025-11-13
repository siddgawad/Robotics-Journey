# robot_coords_step1.py
# Purpose: convert points between robot and world frames using only the two rules:
# (1) rotate by theta, (2) slide by (x, y). No NumPy, no matrices.

import math  # gives us cos, sin, atan2, etc.

def robot_to_world(pose, p_robot):
    """
    Convert a point from robot frame to world frame.

    pose    : (x, y, theta)   robot's position and heading in world
    p_robot : (xr, yr)        point expressed in robot's axes

    Return  : (xw, yw)        same physical point expressed in world axes

    Rule used:
      rotate the point by +theta, then add translation (x, y)
    """
    x, y, theta = pose          # unpack pose tuple
    xr, yr = p_robot            # unpack robot-frame point
    c = math.cos(theta)         # precompute cos(theta)
    s = math.sin(theta)         # precompute sin(theta)

    # Rotate, then translate:
    xw = c * xr - s * yr + x
    yw = s * xr + c * yr + y
    return (xw, yw)

def world_to_robot(pose, p_world):
    """
    Convert a point from world frame to robot frame.

    pose    : (x, y, theta)
    p_world : (xw, yw)

    Return  : (xr, yr)

    Rule used (inverse):
      subtract translation, then rotate by -theta (which is R^T)
    """
    x, y, theta = pose
    xw, yw = p_world
    dx = xw - x                  # vector from robot origin to world point
    dy = yw - y
    c = math.cos(theta)
    s = math.sin(theta)

    # Rotate by -theta: [xr, yr]^T = R^T * [dx, dy]^T
    xr =  c * dx + s * dy
    yr = -s * dx + c * dy
    return (xr, yr)

def _almost_equal(a, b, tol=1e-9):
    return abs(a - b) <= tol

def _check(name, got, expect):
    gx, gy = got
    ex, ey = expect
    ok = _almost_equal(gx, ex) and _almost_equal(gy, ey)
    print(f"{name}: got {got}, expect {expect} -> {'OK' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    # Four sanity checks for cardinal headings.
    ok_all = True

    # θ = 0: just add
    ok_all &= _check("θ=0",
                     robot_to_world((5, -2, 0.0), (3, 4)),
                     (8.0, 2.0))

    # θ = 90°: forward maps to +y, left maps to -x
    ok_all &= _check("θ=90°",
                     robot_to_world((0, 0, math.pi/2), (1, 0)),
                     (0.0, 1.0))

    # θ = 180°: forward -> -x, left -> -y
    ok_all &= _check("θ=180°",
                     robot_to_world((10, -3, math.pi), (2, -5)),
                     (8.0, 2.0))

    # θ = 270°: forward -> -y, left -> +x
    ok_all &= _check("θ=270°",
                     robot_to_world((0, 0, 3*math.pi/2), (0, 4)),
                     (4.0, 0.0))

    # Inverse consistency: world_to_robot should undo robot_to_world
    pose = (3.0, -2.0, 0.3)
    p_r = (0.5, -0.7)
    p_w = robot_to_world(pose, p_r)
    back = world_to_robot(pose, p_w)
    ok_all &= _check("inverse", back, p_r)

    print("RESULT:", "ALL OK" if ok_all else "SOMETHING IS WRONG")
