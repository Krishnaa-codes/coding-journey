# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        else:
            self.direction = NORTH
    def turn_left(self):
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        else:
            self.direction = NORTH
    def advance(self):
        x, y = self.coordinates
        if self.direction == NORTH:
            y += 1
        elif self.direction == EAST:
            x += 1
        elif self.direction == SOUTH:
            y -= 1
        else:
            x -= 1
        self.coordinates = (x, y)

    def move(self, commands):
        for command in commands:
            if command == "R":
                self.turn_right()
            elif command == "L":
                self.turn_left()
            elif command == "A":
                self.advance()