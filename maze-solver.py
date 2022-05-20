import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Define some constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Load the image
img = Image.open("maze.png")

# Get the size of the image
size = img.size

# Get the pixel data from the image
pixels = np.array(img)

# Find the start and end of the maze
start = None
end = None
for row in range(size[0]):
    for col in range(size[1]):
        if np.all(pixels[row, col] == GREEN):
            start = (row, col)
        elif np.all(pixels[row, col] == RED):
            end = (row, col)

# Create a list of all the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Create a list of all the visited nodes
visited = []

# Create a list of all the nodes to visit
to_visit = []

# Add the starting node to the list of nodes to visit
to_visit.append(start)

# Create a dictionary of the node's parents
parents = {}

# Loop until we find the end
while len(to_visit) > 0:
    # Get the node with the lowest cost
    current = to_visit[0]
    current_cost = float("inf")
    for node in to_visit:
        if node[0] + node[1] < current_cost:
            current = node
            current_cost = node[0] + node[1]

    # If the current node is the end, we're done
    if current == end:
        break

    # Remove the current node from the list of nodes to visit
    to_visit.remove(current)

    # Add the current node to the list of visited nodes
    visited.append(current)

    # Loop through the moves
    for move in moves:
        # Get the new row and column
        row = current[0] + move[0]
        col = current[1] + move[1]

        # Make sure the move is valid
        if row < 0 or row >= size[0] or col < 0 or col >= size[1]:
            continue

        # Make sure we haven't visited the node already
        if (row, col) in visited:
            continue

        # Make sure the node isn't a wall
        if np.all(pixels[row, col] == BLACK):
            continue

        # Add the node to the list of nodes to visit
        to_visit.append((row, col))

        # Add the node to the dictionary of parents
        parents[(row, col)] = current

# Create an empty image
img_solution = Image.new("RGB", size)
pixels_solution = np.array(img_solution)

# Loop through the parents dictionary
current = end
while current in parents:
    # Get the parent
    parent = parents[current]

    # Draw a white line on the solution image
    pixels_solution[current[0], current[1]] = WHITE
    pixels_solution[parent[0], parent[1]] = WHITE

    # Set the current node to the parent
    current = parent

# Save the solution image

# NOTE: THIS LINE WAS CREATED BY GPT BUT DOES NOT WORK
# img_solution.save("solution.png") 

# The following line does work
Image.fromarray(pixels_solution).save('solution.png')