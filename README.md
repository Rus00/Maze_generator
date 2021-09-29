# Maze_generator
A program that generates colorful mazes!

This programs uses Prim's algorithm to create random mazes like this:\
![image](https://user-images.githubusercontent.com/49564286/135188563-06dbac9b-14b2-419c-b8ac-61da34ada3b1.png)\
Then it turns them into mazes like this using Jgraph:\
![image](https://user-images.githubusercontent.com/49564286/135188872-acf07466-5f59-4d84-bf46-7588d4de0e3d.png)

If you want a blue maze that is 100 lines by 100 lines, just run ```python maze_gen.py 100 100 -c blue | /home/jplank/bin/LINUX/jgraph | ps2pdf - | convert -density 300 - -quality 100 example.jpg```\
![image](https://user-images.githubusercontent.com/49564286/135189585-eec4c5b2-1e44-4c25-a84c-873dcbfa211b.png)

## To Run
```
python maze_gen.py x y -c color
```
x is the width of the maze.
y is the height of the maze.
color is the color of the maze, which is optional.(Default is black)

```python maze_gen.py -h``` pulls up the help menu.
