"""
Assignment 4: Agent-Based Model for Structural Tessellation Generation

Author: Alberto Martinez

Description:
This script uses a proportional approach to move a list of points down along the Z-axis between two specified distances. 
The script ensures that the first point receives the largest downward translation, while the last point receives the smallest, creating a gradient of movement. 
The movement is calculated proportionally based on the position of each point in the list, with the distance decreasing incrementally from the start to the end point. 
This method is useful for applications where a series of points need to be translated in a structured, gradual manner, such as for simulations or terrain modeling.

Note: This script is intended to be used within Grasshopper's Python scripting component or as a standalone Python script.
"""

import rhinoscriptsyntax as rs

def move_points_z(points, start_z, end_z):
    """
    Moves a list of points down in the Z-axis proportionally between two given distances.
    The first point gets the largest Z translation, the last one gets the smallest.
    """
    # Ensure points are coerced to valid 3D points
    valid_points = []
    
    for pt in points:
        coerced_pt = rs.coerce3dpoint(pt)  # Coerce each point into a valid 3D point
        if coerced_pt:  # If the point is valid
            valid_points.append(coerced_pt)
        else:
            print(f"Invalid point: {pt}")  # Debug: Invalid point

    # Ensure we have at least two valid points
    if len(valid_points) < 2:
        raise ValueError("Input must contain at least two valid points.")
    
    # Calculate the proportional movement for each point
    num_points = len(valid_points)
    distances = [
        start_z + (end_z - start_z) * (i / (num_points - 1))  # Proportional Z movement
        for i in range(num_points)
    ]
    
    # Now move the points
    moved_points = []
    for pt, dist in zip(valid_points, distances):
        moved_point = rs.PointAdd(pt, (0, 0, -dist))  # Move down by dist
        moved_points.append(moved_point)
    
    return moved_points

# Grasshopper Inputs: points, start_z, end_z
if isinstance(points, list):  # Check if points is already a list
    try:
        print("Input points:", points)
        print("Start Z:", start_z, "End Z:", end_z)
        
        # Process the points
        output = move_points_z(points, start_z, end_z)
        
        # Return the moved points
        a = output  # Output the moved points to Grasshopper
    except ValueError as e:
        print(f"Error: {e}")
        a = []  # Return an empty list if error occurs
else:
    print("Error: Points input is not a list.")
    a = []  # Return an empty list if the points are not a list
