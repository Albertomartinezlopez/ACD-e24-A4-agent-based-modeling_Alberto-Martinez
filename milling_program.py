"""
Assignment 4: Agent-Based Model for Structural Tessellation Generation

Author: Alberto Martinez

Description:

This script simulates a milling process using a toolpath and a milling tool, applying a series of boolean difference operations to a block geometry. 
The milling tool is represented as a cylinder with a specified radius and height, and the tool moves along a given curve. 
By dividing the toolpath into discrete points, the script progressively subtracts material from the block at each point along the path, resulting in a new, milled geometry. 
This method provides a way to visualize the effect of the milling process, allowing exploration of how varying tool parameters and toolpath shapes influence the final form.

Note: This script is intended to be used within Grasshopper's Python scripting component or as a standalone Python script.
"""

import Rhino.Geometry as rg

# Define the Agent class to represent the milling tool
class Agent:
    def __init__(self, tool_radius, tool_height):
        # Initialize the agent with tool radius and height
        self.tool_radius = tool_radius
        self.tool_height = tool_height
        self.tool = rg.Cylinder(rg.Circle(self.tool_radius), self.tool_height)  # Create the milling tool

    def move_to(self, point):
        # Move the agent (tool) to a new position (point)
        translation_vector = rg.Vector3d(point.X, point.Y, point.Z)
        tool_move = rg.Transform.Translation(translation_vector)
        
        moved_tool = self.tool.ToBrep(True, True)  # Create the Brep and cap the cylinder ends
        moved_tool.Transform(tool_move)  # Move the tool to the new position
        return moved_tool

# Inputs:
# block_geometry (BRep): The original block geometry to be milled
# toolpath_curve (Curve): The toolpath curve along which the tool moves
# tool_radius_value (float): The radius of the milling tool (cylinder radius)
# tool_height_value (float): The height (depth) of the milling tool (cylinder height)

# The input variables from Grasshopper will be used here:
block = block_geometry  # BRep geometry of the block to be milled
toolpath = toolpath_curve  # The toolpath curve where the tool moves
tool_radius = tool_radius_value  # Radius of the milling tool (cylinder radius)
tool_height = tool_height_value  # Height of the milling tool (cylinder height)

# Create the milling agent (tool)
agent = Agent(tool_radius, tool_height)

# Create a list of points along the toolpath
# Divide the toolpath curve into a number of points (e.g., divide into 100 segments)
toolpath_points = [toolpath.PointAt(t) for t in range(0, 101)]

# Set the initial block as the result block
result_block = block

# Loop over the points along the toolpath and subtract material
for point in toolpath_points:
    # Move the agent (tool) to the current point
    moved_tool = agent.move_to(point)  # Get the moved tool at the current point
    
    # Perform the boolean difference (subtract the tool from the block)
    result_block = rg.Brep.CreateBooleanDifference([result_block] + [moved_tool])[0]

# Output the resulting block after milling
resulting_block = result_block  # The new BRep after the milling operation
