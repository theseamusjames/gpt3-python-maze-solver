# gpt3-python-maze-solver
I asked GPT-3 to write a program to solve a maze. It did.

See it in [the playground](https://beta.openai.com/playground/p/wNiL2BaK2bUVTwMx36HH5lPV).

# How to use

1. Clone the repo. 
2. `cd gpt3-python-maze-solver`
3. `python maze-solver.py && open solution.png`

# Instructions provided to GPT-3
```
Image of maze:
The maze walls will be black
The maze path will be white
The maze start will be a green pixel
The maze end will be a red pixel

Write a python program that does the following:
Load an image of a maze from the file "maze.png". It will meet the description of the maze above.
Analyze the image to find a solution to the maze. Use the a* pathfinding algorithm.
Produce an image which has a line drawing of the solution to the maze.

### Python code:
```
# Bugs
This solution it created had one bug, at the very last line where it attempted to save the image of the solution. I fixed it, and that was the only change.

It took several tries to get a version that worked, but this one did. It does not employ the A* algorithm, but it does find a solutiuon.
