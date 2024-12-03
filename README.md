# Assignment 4: Agent-Based Model for Structural Tessellation Generation

![Example Structural Tessellation](images/structural_tessellation.jpg)

## Objective

In this final assignment, you will harness the power of **Object-Oriented Programming (OOP)** and **agent-based modeling** to create complex structural patterns. You are encouraged to align this project with your studio or research work, exploring how agent-based algorithms can inform architectural form generation.

Your task is to:

- Design and implement classes and objects following the OOP paradigm to represent agents and their behaviors.
- Use algorithms to control the behavior of agents and the evolution of patterns over time.
- Explore how changes in the rules or parameters affect the form.
- Produce a series of 3D models that illustrate the application of agent-based algorithms to form generation.

---

## Table of Contents

- [Tasks](#tasks)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Instructions](#instructions)
- [Ideas for Exploration](#ideas-for-exploration)
- [Submission Guidelines](#submission-guidelines)
- [Evaluation Criteria](#evaluation-criteria)
- [Resources](#resources)
- [Contact](#contact)

---

## Tasks

1. **Design and Implement an Agent-Based Model**

   - Create a Python script (agent_based_model.py) that implements an agent-based model using OOP principles.
   - Define classes to represent agents and encapsulate their behaviors and interactions.
   - Implement algorithms that govern agent behaviors and how they affect the generation of structural patterns.
   - Ensure that your model can evolve over time, allowing agents to interact and create complex forms.

2. **Explore Parameter Variations**

   - Experiment with different rules, parameters, and initial conditions.
   - Analyze how changes in agent behaviors influence the resulting patterns.
   - Document your findings and include visual examples of different outcomes.

3. **Align with Personal Interests**

   - Tailor your project to align with your studio work, research interests, or a particular area you wish to explore.
   - Consider alternative challenges beyond structural tessellation, such as:

     - **Environmental Simulation**: Agents representing environmental factors influencing form.
     - **Crowd Simulation**: Modeling pedestrian flows in architectural spaces.
     - **Growth Patterns**: Biomimetic growth algorithms for structural elements.
     - **Interactive Systems**: Agents responding to user input or sensor data.

4. **Documentation**

   - Write detailed pseudo-code explaining your classes and algorithms in DOCUMENTATION.md.
   - Provide technical explanations of your design choices and how OOP principles are applied.
   - Include a report discussing the rationale behind the chosen rules and their impact on the final model.
   - Insert images of your generated models into the documentation.

---

## Getting Started

### Prerequisites

- **Rhinoceros 3D** with **Grasshopper** plugin 
- **Python scripting in Grasshopper** or standalone **Python 3.x**
- Familiarity with **Object-Oriented Programming** concepts
- **Rhino.Geometry** and **RhinoScriptSyntax** modules
- Alternatively, any 3D visualization library compatible with Python (e.g., **Blender's bpy**, **matplotlib**, **PyOpenGL**, **Processing.py**)

### Software Installation

- Ensure you have the necessary software installed for your chosen development environment.
- Install any additional libraries or dependencies required for your project.

---

## Repository Structure
```
Assignment4/
├── README.md               # Assignment handout (this file)
├── DOCUMENTATION.md        # Documentation with pseudo-code and explanations
├── agent_based_model.py    # Python script for agent-based model
├── images/
│   └── (Output Images)
└── src/
    ├── helper_functions.py # Helper functions
    └── (Additional scripts or components)
```

---

## Instructions

1. **Clone the Repository**

   - Accept the assignment on GitHub Classroom and clone the repository to your local machine.

2. **Plan Your Project**

   - Decide on the focus of your agent-based model.
   - Sketch out ideas and consider how OOP principles will be applied.
   - Identify the agents, their properties, and behaviors.

3. **Implement the Agent-Based Model**

   - **Define Agent Classes**:

     - Create classes representing agents with attributes and methods.
     - Consider inheritance and polymorphism if appropriate.

   - **Implement Behaviors and Interactions**:

     - Define how agents interact with each other and their environment.
     - Use algorithms to govern agent behaviors (e.g., rules, state machines, decision trees).

   - **Model Evolution Over Time**:

     - Implement a simulation loop or time-stepping mechanism.
     - Allow agents to update their state and influence the model over time.

   - **Visualization**:

     - Use Rhino/Grasshopper, Blender, or any suitable platform to visualize the results.
     - Ensure that the generated models effectively communicate the agent behaviors and resulting patterns.

4. **Experiment with Parameters**

   - Create parameters that can be adjusted to alter agent behaviors.
   - Experiment with different values and document the effects on the final model.
   - Consider implementing user input mechanisms to facilitate exploration.

5. **Align with Personal Interests**

   - Adapt the project to align with your studio or research work.
   - Feel free to explore alternative challenges or extend the scope of the project.

6. **Document Your Work**

   - Write detailed pseudo-code in DOCUMENTATION.md explaining your classes and algorithms.
   - Provide technical explanations and discuss how OOP principles are applied.
   - Include images and explanations of different design variations.
   - Discuss any challenges faced and how you overcame them.

7. **Version Control with Git**

   - Make regular commits with meaningful messages.
   - Push your commits to the GitHub repository.

8. **Review and Finalize**

   - Ensure your code is well-commented and organized.
   - Verify that all generated images are saved correctly.
   - Double-check your documentation for clarity and completeness.

---

## Ideas for Exploration

To challenge yourself and expand the scope of your project, consider exploring the following ideas:

- **Advanced Agent Behaviors**:

  - Implement complex decision-making processes using artificial intelligence techniques.
  - Use neural networks, genetic algorithms, or reinforcement learning to govern agent behaviors.

- **Multi-Agent Systems**:

  - Create a system with different types of agents interacting.
  - Explore emergent behaviors resulting from agent interactions.

- **Environmental Interaction**:

  - Allow agents to respond to environmental data (e.g., site context, environmental simulations).
  - Integrate sensors or external data sources to influence agent behaviors.

- **User Interaction**:

  - Develop an interactive application where users can influence the simulation in real-time.
  - Implement GUI elements or use interactive sliders in Grasshopper.

- **Cross-Disciplinary Applications**:

  - Apply agent-based modeling to areas such as urban planning, ecology, or social systems.
  - Explore how agent behaviors can simulate real-world phenomena.

- **Optimization and Performance**:

  - Optimize your code for performance, especially if dealing with large numbers of agents.
  - Explore parallel computing or optimized data structures.

---

## Submission Guidelines

- **What to Submit**:

  - Your agent_based_model.py script and any additional scripts in the src/ directory.
  - Completed DOCUMENTATION.md with pseudo-code, explanations, and images.
  - Generated images saved in the images/ folder.
  - Any additional documentation or resources in the docs/ folder.

- **Submission Checklist**:

  - [ ] Code runs without errors.
  - [ ] Code is well-commented and follows best practices.
  - [ ] DOCUMENTATION.md is complete and thorough.
  - [ ] Visualizations of different outcomes are saved and referenced in your documentation.
  - [ ] All changes are committed with meaningful messages and pushed to your GitHub repository.

---

## Evaluation Criteria

- **Implementation and Functionality**

  - Effective use of OOP principles in the design of the agent-based model.
  - Correct implementation of agent behaviors and interactions.
  - Ability of the model to evolve over time and generate structural patterns.

- **Design Exploration**

  - Creativity and originality in agent behaviors and resulting patterns.
  - Exploration of parameter variations and their impact.

- **Technical Understanding**

  - Demonstrated understanding of OOP concepts and agent-based modeling.
  - Clear explanations in code comments and documentation.

- **Code Quality**

  - Clean, readable, and well-organized code.
  - Use of meaningful variable names and proper formatting.

- **Documentation**

  - Detailed pseudo-code and technical explanations.
  - Inclusion and discussion of generated design variations.
  - Discussion of challenges and solutions.

- **Use of Git and Version Control**

  - Regular commits with meaningful messages.
  - Proper repository structure and organization.

---

## Resources

- **Object-Oriented Programming in Python**

  - [Official Python Tutorial - Classes](https://docs.python.org/3/tutorial/classes.html)
  - [Real Python - Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)

- **Python in Rhino and Grasshopper**
  - [Rhino.Python Guides](https://developer.rhino3d.com/guides/rhinopython/)
  - [RhinoScriptSyntax](https://developer.rhino3d.com/api/RhinoScriptSyntax/)

---

## Contact

If you have any questions or need assistance, please reach out to the instructor via email or the course forum.

---