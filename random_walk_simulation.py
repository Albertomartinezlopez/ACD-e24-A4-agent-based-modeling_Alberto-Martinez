"""
Assignment 4: Agent-Based Model for Structural Tessellation Generation

Author: Alberto Martinez

Description:
This script implements a random walk simulation on a surface using Object-Oriented Programming (OOP) principles. It defines a "Walker" class that moves along the surface based on random steps in both the u and v directions of the surface's parameter space. The walker starts at the center of the surface and iteratively adjusts its position, staying within the defined surface boundaries. The result is a series of points generated over time, simulating the path taken by the walker as it explores the surface. This approach allows for exploration of the surface and can be adapted to study how different surface geometries and step sizes influence the resulting path.

Note: This script is intended to be used within Grasshopper's Python scripting component or as a standalone Python script.
"""

import rhinoscriptsyntax as rs
import random as r

# Set the random seed for reproducibility
r.seed(seed)

# Define the Walker class
class Walker:

    def __init__(self, surface):
        # Initialize the surface and position of the walker
        self.surface = surface
        u_domain = rs.SurfaceDomain(surface, 0)
        v_domain = rs.SurfaceDomain(surface, 1)
        # Start at the center of the surface
        self.u = (u_domain[0] + u_domain[1]) / 2
        self.v = (v_domain[0] + v_domain[1]) / 2

    def step(self):
        # Randomly adjust the u and v parameters within the surface domain
        u_domain = rs.SurfaceDomain(self.surface, 0)
        v_domain = rs.SurfaceDomain(self.surface, 1)
        
        du = r.uniform(-5, 5)  # Small random step in u
        dv = r.uniform(-5, 5)  # Small random step in v

        # Update the position while ensuring it stays within the surface domain
        self.u = max(min(self.u + du, u_domain[1]), u_domain[0])
        self.v = max(min(self.v + dv, v_domain[1]), v_domain[0])

    @property
    def point(self):
        # Evaluate the surface at the current u and v parameters to get the 3D point
        return rs.EvaluateSurface(self.surface, self.u, self.v)

# Create a walker instance starting on the input surface
w = Walker(surface)

# List to store points
pList = []

# Iterate for the given number of time steps
for t in range(time):
    w.step()  # Update the walker's position
    pList.append(w.point)  # Add the current position to the list

# Output the list of points
a = [rs.AddPoint(p) for p in pList]  # Visualize points in Rhino
