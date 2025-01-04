# Assignment 4: Agent-Based Model Documentation


The agent-based models documented here are based on a research project that explores the bioreceptivity of artificial reefs, focusing on the interactions between marine structures and the small fauna and flora that colonize them. Through computational simulations inspired by agent-based modeling, we investigate how environmental factors, surface geometries, and random movements of small marine organisms influence the development of bioreceptive patterns over time.

The first program simulates agents traversing complex surfaces, mimicking the movements of marine organisms as they explore and attach to the reef structure. The second program models the gradual transformation of these surfaces, translating ecological interactions into proportional movements that shape the reef's micro-topography. The third program integrates toolpath-like milling strategies, representing the biological and physical forces eroding or modifying the reef's surfaces. Together, these simulations provide a framework to analyze and predict the dynamic relationship between artificial reef structures and their colonizing biota, aiding the design of reefs that foster enhanced ecological integration and bioreceptivity in marine environments.

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Design Variations](#design-variations)
- [Challenges and Solutions](#challenges-and-solutions)
- [References](#references)

---

## Pseudo-Code

### Walker Agent:

1. **Main Simulation Loop**:
  - Initialize Walker object with surface.
  - Loop through time steps:
      - Call step() method to update walker's position.
      - Append updated position (point) to pList.

2. **Walker Class**:
  - **Attributes**:
    - surface: The surface on which the walker moves.
    - u, v: Parameters representing the walker's current position on the surface.
  - **Methods**:
    **__init__(surface)**:
      - Get surface domains (u and v).
      - Set initial walker position to the center of the surface.
    **step()**:
      - Adjust u and v randomly within their respective domains.
    **point()**:
      - Evaluate the surface at the walker’s (u, v) parameters to get the corresponding 3D point.

3. **Main Process**:
  - Initialize walker on surface.
  - Loop through each time step:
  - Update walker's position.
  - Add the new position to a list of points.
  - Output the list of points to visualize the random walk.


### Point gradual translator:

1. **Main Process**

  - **Initialize Input Data**:
      Receive a list of points, start_z, and end_z as inputs.
  - **Coerce Points**:
    Ensure that all points are valid 3D points by coercing them into valid geometry.
    If a point is invalid, print an error message and skip it.
  - **Check Point Validity**:
    Ensure there are at least two valid points in the list.
    If not, raise an error (ValueError) indicating that at least two valid points are needed.
  - **Calculate Proportional Z-Translation**:
    For each point, calculate the proportional Z-axis translation based on the input start_z and end_z.
    The first point will have the largest Z translation (based on start_z), and the last point will have the smallest Z translation (based on end_z).
  - **Move Points**:
    For each valid point, apply the proportional Z translation calculated in the previous step.
    Store the moved points in a list.
  - **Return Moved Points**:
    Output the list of moved points as the result.

2. **Helper Functions and Flow**
  - **move_points_z Method**:
    **Inputs**:
    - points: List of 3D points to be moved.
    - start_z: Starting Z value (largest Z translation).
    - end_z: Ending Z value (smallest Z translation).
    **Outputs**:
      A list of moved points after applying the proportional Z translation.
    **Steps**:
      Loop through each point in the input list:
      - Coerce the Point: Ensure the point is valid in 3D space.
      - Check Validity: Ensure there are at least two valid points.
      - Calculate Proportional Movement: For each point in the list, calculate its Z translation based on its position in the list (more distant points move further).
      - Move the Points: Apply the calculated Z translation to each point and store the results.
      - Return the moved points.

3. **Error Handling**
    If the input points is not a list or contains fewer than two valid points, print an error message and return an empty list.
 
### Milling Program:

1. **Main Milling Process**

  - **Initialize Milling Tool (Agent)**:
    - Create an instance of the Agent class with tool radius and height.
  - **Create Toolpath**:
    - Divide the toolpath curve into discrete points (e.g., 100 segments).
  - **Milling Loop**:
    For each point in the toolpath:
      - Move Tool (Agent):
        - Move the milling tool (agent) to the current point on the toolpath.
      - Subtract Material:
        - Perform a boolean difference operation to subtract the milling tool (cylinder) from the block geometry.
  - **Final Output**:
    Output the final geometry after milling.

2. **Agent Class**

  **Attributes**:
    - **tool_radius**: The radius of the milling tool (cylinder radius).
    - **tool_height**: The height (depth) of the milling tool (cylinder height).
    - **tool**: The milling tool represented as a cylinder (created using the radius and height).
  **Methods**:
  - **move_to(point)**: 
    - Moves the milling tool (agent) to a specified point along the toolpath.
    - Translates the tool to the point's position in 3D space.
  - **generate_tool()**:
    - Generates the milling tool (cylinder) at a specific position and returns it as a Brep (solid geometry).

3. **Main Steps**

  **Inputs**:
    - block_geometry: The original geometry of the block to be milled (BRep).
    - toolpath_curve: The curve along which the tool will move (Curve).
    - tool_radius_value: The radius of the milling tool.
    - tool_height_value: The height of the milling tool.
  - **Create Milling Tool**:
    Initialize an Agent object with the given tool_radius_value and tool_height_value.
  - **Create Toolpath Points**:
    Divide the toolpath curve into multiple points for the tool to follow (e.g., 100 points).
  - **Loop Through Toolpath**:
   - For each point in the toolpath:
     - Move the tool (agent) to the current point.
     - Subtract the tool (milling tool) from the block geometry using a boolean difference operation.
  - **Output**:
    Return the resulting geometry after the milling operation.

4. **Final Result**

  **Result Block**:
  The modified block geometry after all milling steps have been performed, representing the final output after subtracting material along the toolpath.

---

## Technical Explanation

*(Provide a concise explanation of your code, focusing on how you implemented OOP principles and agent-based modeling. Discuss how your approach generates the final structural patterns and the mathematical or computational principles involved.)*

### Topics to Cover:

- **Object-Oriented Design**

  - Explain the classes you designed and why.
  - Discuss how you applied OOP principles like encapsulation, inheritance, and polymorphism.
  - Describe how the classes interact within the simulation.

- **Agent Behaviors and Interactions**

  - Describe the rules governing agent behaviors.
  - Explain how agents interact with each other and the environment.
  - Discuss any algorithms or decision-making processes implemented.

- **Simulation Loop**

  - Explain how the simulation evolves over time.
  - Describe how time-stepping or iteration is handled.
  - Discuss any performance considerations.

- **Visualization**

  - Explain how the agent data is used to generate the final models.
  - Discuss any visualization techniques or tools used.

---

## Design Variations

*(Include images and descriptions of your generated design variations. For each variation, discuss the parameters or rules changed and the impact on the resulting patterns.)*

### Variation Examples

1. **Variation 1: [Name/Description]**

   ![Variation 1](images/variation1.jpg)

   - **Parameters Changed**:
     - interaction_radius: [Value]
     - alignment_strength: [Value]
   - **Description**:
     - Describe how these changes affected agent behaviors and the final pattern.

2. **Variation 2: [Name/Description]**

   ![Variation 2](images/variation2.jpg)

   - **Parameters Changed**:
     - cohesion_factor: [Value]
     - separation_distance: [Value]
   - **Description**:
     - Discuss the observed changes in the model.

3. **Variation 3: [Name/Description]**

   ![Variation 3](images/variation3.jpg)

   - **Parameters Changed**:
     - randomness: [Value]
     - environmental_influence: [Value]
   - **Description**:
     - Explain how the introduction of randomness or environmental factors impacted the results.

*(Add more variations as needed.)*

---

## Challenges and Solutions

*(Discuss any challenges you faced during the assignment and how you overcame them.)*

### Examples:

- **Challenge 1**: Managing large numbers of agents efficiently.
  - **Solution**: Implemented spatial partitioning to reduce computation time.

- **Challenge 2**: Agents getting stuck or clustering unnaturally.
  - **Solution**: Adjusted interaction rules and added collision avoidance behaviors.

- **Challenge 3**: Visualizing the simulation in real-time.
  - **Solution**: Used efficient data structures and optimized rendering techniques.

---

## References

*(List any resources you used or found helpful during the assignment.)*

- **Object-Oriented Programming**

  - [Python Official Documentation](https://docs.python.org/3/tutorial/classes.html)
  - [Real Python - OOP in Python](https://realpython.com/python3-object-oriented-programming/)

- **Agent-Based Modeling**

  - [Mesa: Agent-Based Modeling in Python](https://mesa.readthedocs.io/en/master/)
  - [Agent-Based Models in Architecture](https://www.researchgate.net/publication/279218265_Agent-based_models_in_architecture_new_possibilities_of_interscalar_design)

- **Visualization Tools**

  - [Rhino.Python Guides](https://developer.rhino3d.com/guides/rhinopython/)
  - [matplotlib](https://matplotlib.org/)
  - [Blender Python API](https://docs.blender.org/api/current/)

---

*(Feel free to expand upon these sections to fully capture your work and learning process.)*

---