from turtle import  Turtle, Screen

BLOCKS_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.all_blocks = []
        self.create_snake()
        self.head = self.all_blocks[0]

    def create_snake(self):
        for coordinates in BLOCKS_COORDINATES:
            new_block = Turtle(shape='square')
            new_block.color('white')
            new_block.penup()
            new_block.goto(coordinates)
            self.all_blocks.append(new_block)

    def move(self):
        for turtle in range(len(self.all_blocks) - 1, 0, -1):
            next_x_cor = self.all_blocks[turtle - 1].xcor()
            next_y_cor = self.all_blocks[turtle - 1].ycor()
            self.all_blocks[turtle].goto(next_x_cor, next_y_cor)

        self.all_blocks[0].forward(MOVE_DISTANCE)

    def update_snake_length(self):
        new_block = Turtle(shape='square')
        new_block.color('white')
        new_block.penup()
        new_block.goto(self.all_blocks[-1].position())
        self.all_blocks.append(new_block)


    def check_collision(self):
        for blocks in self.all_blocks[1:]:
            # if blocks == self.head:
            #     pass
            # el
            if self.head.distance(blocks) < 10:
                return False
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)