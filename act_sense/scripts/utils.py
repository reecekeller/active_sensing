import numpy as np
from scripts.arena import Arena, Aperture, Mouse, visualize_arena
from tqdm import tqdm 
import numpy as np

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


def get_visible_angles(source, circle_center, radius, aperture):
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
    #print(len(angles), len(visible_angles))
    #area  = get_segment_area(visible_angles, radius)
    return visible_angles

def get_segment_area(angles, radius):
    if len(angles)==0:
        return (0, 0)
    else:
        # Sort the angles
        angles = np.sort(angles)
        # Calculate the differences between consecutive angles
        if (0 in angles):
            diffs = np.diff(angles, append=angles[-1]-angles[0])# + 2 * np.pi - angles[-1])
        else:
            diffs = np.abs(np.diff(angles, append=angles[0]))
        # Find the largest gap, which is the central angle of the segment
        central_angle = np.max([np.max(diffs), np.min(diffs)])
        #print(central_angle)
        # Calculate the area of the circular segment
        # Area of segment = 0.5 * radius^2 * (theta - sin(theta))
        area = 0.5 * radius**2 * (central_angle - np.sin(central_angle))

        # area compliment 
        area_c = np.abs(np.pi*radius**2 - area)
        return np.array([area, area_c])

def infoMetric(area1, area2):
    return 0.5 * np.abs(area1 + area2)

def info_map(arena, circle1_center, circle2_center, aperture, radius):
    x_resolution = arena.width
    y_resolution = arena.length - aperture.gap_width

    x = np.linspace(0, arena.length, x_resolution)
    y = np.linspace(0, arena.width, y_resolution)

    info_mat = np.zeros((x_resolution, y_resolution))
    print(info_mat.shape, '\n')
    # Iterate through a grid of points in the arena
    for i in tqdm(range(x_resolution)):
        for j in range(y_resolution):
            source = (x[i], y[j], 20)
            visible_anglesL = get_visible_angles(source, circle1_center, radius, aperture)
            visible_anglesR = get_visible_angles(source, circle2_center, radius, aperture)

            area_circle1 = get_segment_area(visible_anglesL, radius)
            area_circle2 = get_segment_area(visible_anglesR, radius)

            # Check whether to use major or minor segment area

            # larger element of area_circle is last element
            if source[0] > arena.length/2:
                A1 = np.max(area_circle1)
                A2 = np.min(area_circle2)
            elif source[0] < arena.length/2:
                A1 = np.min(area_circle1)
                A2 = np.max(area_circle2)
            else: 
                A1 = area_circle1[0]
                A2 = area_circle2[0]    

            info_mat[i, j] = infoMetric(A1, A2) 
    return info_mat