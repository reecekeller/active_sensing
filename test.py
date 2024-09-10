import numpy as np
from arena import Arena, Aperture, visualize_arena, Mouse

import matplotlib.pyplot as plt

d_theta = np.pi/180  # Increase for higher accuracy
angles = np.arange(0, 2 * np.pi, d_theta)


def get_visibility(source, target, aperture):
    v_t2Lwall = np.subtract(aperture.left_wall_edge + (target[2],), target)
    v_t2Lwall = v_t2Lwall/np.linalg.norm(v_t2Lwall)
    v_t2Rwall = np.subtract(aperture.right_wall_edge + (target[2],), target)
    v_t2Rwall = v_t2Rwall/np.linalg.norm(v_t2Rwall)

    # Vector from target to source (normalized)
    v_t2s = np.subtract(source, target)
    v_t2s = v_t2s / np.linalg.norm(v_t2s)

    # Cross products to determine the relative position of v_target2source
    cross_LS = np.cross(v_t2Lwall[:2], v_t2s[:2])
    cross_RS = np.cross( v_t2s[:2], v_t2Rwall[:2],)
    # Check if v_target2source is between the left and right wall vectors

    if cross_LS >=0 and cross_RS >=0:
        return True
    else:
        return False


def get_visible_area(source, circle_center, radius, aperture):
    """
    Calculate the visible area of a circle from a given point by checking the visibility
    of various points on the circle's perimeter.
    """
    d_theta = np.pi/180  # Increase for higher accuracy
    angles = np.arange(0, 2 * np.pi, d_theta)
    visible_angles = []
    
    for i in range(len(angles)-1):
        # Parametrize the circle
        x_circle = circle_center[0] + radius * np.cos(angles[i])
        z_circle = circle_center[2] + radius * np.sin(angles[i])
        y_circle = circle_center[1]  # Y remains the same for a circle in the YZ plane
        
        circle_point = (x_circle, y_circle, z_circle)
        flag = get_visibility(source, circle_point, aperture)
        if flag:
            visible_angles.append(angles[i])
    print(len(angles), len(visible_angles))
    area  = get_segment_area(visible_angles, radius)
    return area

def get_segment_area(angles, radius):
    if len(angles)==0:
        return (0, 0)
    else:
        # Sort the angles
        angles = np.sort(angles)
        
        # Calculate the differences between consecutive angles
        diffs = np.diff(angles, append=angles[0] + 2 * np.pi - angles[-1])
        
        # Find the largest gap, which is the central angle of the segment
        central_angle = np.max(diffs)
            
        # Calculate the area of the circular segment
        # Area of segment = 0.5 * radius^2 * (theta - sin(theta))
        area = 0.5 * radius**2 * (central_angle - np.sin(central_angle))

        # area compliment 
        area_c = np.pi*radius**2 - area
        return (area, area_c)
#x = get_visible_area(angles, 1)

source = (30, 0, 20)
target = (25, 60, 25)
arena = Arena(length=60, width=60, height=50)
aperture = Aperture(arena_width=60, arena_height=50, arena_length=60, gap_width=10)
circleL = (arena.width/2 - aperture.gap_width, arena.width, arena.height/2)
circleR = (arena.width/2 + aperture.gap_width, arena.width, arena.height/2)

print(circleL, circleR)
#print("target", target)
#print('source', source)
flag = get_visibility(source, target, aperture)
#flag = tup[0]; x = tup[1]; y = tup[2]
print(flag)#[0], flag[1]*180/np.pi, flag[2]*180/np.pi)
# should use right most point on perim of circle as target
#tup = get_visibility(point, circle1_center, aperture, shape_id='left')
#flag = tup[0]; x = tup[1]; y = tup[2]
#print(flag, x, y, x, y)

areaL = get_visible_area(source, circleL, 2, aperture)
areaR = get_visible_area(source, circleR, 2, aperture)
print(areaL, areaR)

mouse = Mouse(*source)  # Initial mouse position
visualize_arena(arena, mouse, aperture)
