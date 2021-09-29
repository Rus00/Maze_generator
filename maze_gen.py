import random
import sys
import argparse
from matplotlib import colors

class Maze:
    def __init__(self, y, x):
        self.width = x
        self.height = y

        self.cell = 'c'
        self.wall = 'w'

    def count_surrounding(self, rand_wall):
        count = 0

        if (self.maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
            count += 1
        if (self.maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
            count += 1
        if (self.maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
            count += 1
        if (self.maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            count += 1
        return count

    def get_maze(self):
        # Initialize the maze
        self.maze = [["u" for i in range(self.width)] for j in range(self.height)]
        walls = []

        starting_x = int(random.random() * self.width)
        starting_y = int(random.random() * self.height)

        if starting_x == 0:
            starting_x += 1
        elif starting_x == self.width - 1:
            starting_x -= 1

        if starting_y == 0:
            starting_y += 1
        elif starting_y == self.height - 1:
            starting_y -= 1

        self.maze[starting_y][starting_x] = self.cell

        walls.append((starting_y - 1, starting_x))
        walls.append((starting_y + 1, starting_x))
        walls.append((starting_y, starting_x - 1))
        walls.append((starting_y, starting_x + 1))

        self.maze[starting_y - 1][starting_x] = self.wall
        self.maze[starting_y + 1][starting_x] = self.wall
        self.maze[starting_y][starting_x - 1] = self.wall
        self.maze[starting_y][starting_x + 1] = self.wall

        while(len(walls) > 0):
            rand_wall = walls[int(random.random() * len(walls)) - 1]

            # Check if the wall is on one of the left or right edges.
            if rand_wall[1] != 0 and rand_wall[1] != self.width-1:
                # Check if the wall has both undefined and cell on its left and right side.
                if self.maze[rand_wall[0]][rand_wall[1]-1] == 'u' and self.maze[rand_wall[0]][rand_wall[1]+1] == 'c' or self.maze[rand_wall[0]][rand_wall[1]-1] == 'c' and self.maze[rand_wall[0]][rand_wall[1]+1] == 'u':
                    # Check if the wall has at least 2 cells surrounding it.
                    if(self.count_surrounding(rand_wall) < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = 'c'
                        # Check if the wall is on top or bottom edge.
                        if(rand_wall[0] != 0 and rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0]-1][rand_wall[1]] == 'u'):
                                self.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                                if ((rand_wall[0]-1, rand_wall[1]) not in walls):
                                    walls.append((rand_wall[0]-1, rand_wall[1]))

                            if (self.maze[rand_wall[0]+1][rand_wall[1]] == 'u'):
                                self.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                                if ((rand_wall[0]+1, rand_wall[1]) not in walls):
                                    walls.append((rand_wall[0]+1, rand_wall[1]))

                        # Check if the left side is undefined
                        if (self.maze[rand_wall[0]][rand_wall[1]-1] == 'u'):
                            self.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                        # Check if the right side is undefined
                        if (self.maze[rand_wall[0]][rand_wall[1]+1] == 'u'):
                            self.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
            
            if rand_wall[0] != 0 and rand_wall[0] != self.height-1:
                # Check if the wall has both undefined and cell on its top and bottom side.
                if self.maze[rand_wall[0]-1][rand_wall[1]] == 'u' and self.maze[rand_wall[0]+1][rand_wall[1]] == 'c' or self.maze[rand_wall[0]-1][rand_wall[1]] == 'c' and self.maze[rand_wall[0]+1][rand_wall[1]] == 'u':
                    # Check if the wall has at least 2 cells surrounding it.
                    if(self.count_surrounding(rand_wall) < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = 'c'
                        # Check if the wall is on left or right edge.
                        if(rand_wall[1] != 0 and rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1]-1] == 'u'):
                                self.maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                                if ((rand_wall[0], rand_wall[1]-1) not in walls):
                                    walls.append((rand_wall[0], rand_wall[1]-1))

                            if (self.maze[rand_wall[0]][rand_wall[1]+1] == 'u'):
                                self.maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                                if ((rand_wall[0], rand_wall[1]+1) not in walls):
                                    walls.append((rand_wall[0], rand_wall[1]+1))

                        # Check if the top side is undefined
                        if (self.maze[rand_wall[0]+1][rand_wall[1]] == 'u'):
                            self.maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                        # Check if the bottom side is undefined
                        if (self.maze[rand_wall[0]-1][rand_wall[1]] == 'u'):
                            self.maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

            walls.remove(rand_wall)
                
                        

        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = 'w'
           
        for i in range(0, self.width):
            if (self.maze[1][i] == 'c'):
                self.maze[0][i] = 'c'
                break

        for i in range(self.width-1, 0, -1):
            if (self.maze[self.height-2][i] == 'c'):
                self.maze[self.height-1][i] = 'c'
                break



        return self.maze

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Maze generator.')
    parser.add_argument('Width', type=int, help="The width of the maze.")
    parser.add_argument('Height', type=int, help="The height of the maze.")
    parser.add_argument('-c', '--color', type=str, help="The color of the maze.")
    args = parser.parse_args()


    width = args.Width
    height = args.Height
    mazeGen = Maze(height, width)
    maze = mazeGen.get_maze()

    print("newgraph")
    print("xaxis min", -10, "size", 7)
    print("yaxis min", -10, "size", 7)

    # print('xaxis size', 7)
    # print('yaxis size', 7)

    # print("X", width + 10)
    # print("Y", height + 10)

    for y, row in enumerate(maze):
        countW = 0
        for x, value in enumerate(row):
            if(value == 'w'):
                if(countW == 0):
                    print("newline", end = ' ')
                    
                    if args.color:
                        rgb = colors.to_rgb(args.color)
                        print('color', rgb[0], rgb[1], rgb[2], end = ' ')

                    print("pts", x + 1, height - y)
                countW += 1
            else:
                if(countW > 1):
                    print(x, height - y)
                countW = 0
            
            if(x == width - 1):
                if(countW > 1):
                    print(x + 1, height - y)
                countW = 0
    
    for x in range(width):
        countW = 0
        for y in range(height):
            # print('x:', x)
            # print('y:', y)
            if(maze[y][x] == 'w'):
                if(countW == 0):
                    print("newline", end = ' ')
                    
                    if args.color:
                        rgb = colors.to_rgb(args.color)
                        print('color', rgb[0], rgb[1], rgb[2], end = ' ')

                    print("pts", x + 1, height - y)
                countW += 1
            else:
                if(countW > 1):
                    print(x + 1, height - y + 1)
                countW = 0

            if(y == height - 1):
                if(countW > 1):
                    print(x + 1, height - y)
                countW = 0


    #print('\n'.join(map(' '.join, maze)))