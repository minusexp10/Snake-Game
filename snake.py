from turtle import Turtle, Screen

screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

PLAY_X = 230  # 265 FOR SCREEN ON 600X600
PLAY_Y = 230


def playground():
    referee = Turtle()
    referee.speed("fastest")
    referee.hideturtle()
    referee.pencolor("white")
    referee.pu()
    referee.goto(-PLAY_X, -PLAY_Y)
    referee.pd()
    for _ in range(4):
        referee.forward(460)  # 530 FOR SCREEN @600X600
        referee.left(90)


class Snake:

    def __init__(self, size):
        # Screen Setup
        screen.setup(width=500, height=500)
        screen.bgcolor("black")
        screen.title("Snake Game")
        screen.tracer(0)
        screen.listen()
        playground()

        # Basic initializations
        self.size = size
        self.snakes = []
        # self.create_snake()
        self.head = ''

    def create_snake(self):
        x = 0
        for i in range(3):
            obj = Turtle("square")
            obj.color("white")
            obj.penup()
            obj.speed("slow")
            obj.shapesize(stretch_wid=self.size, stretch_len=self.size)
            obj.goto(x=x, y=0)
            x -= self.size * 20
            self.snakes.append(obj)
        self.head = self.snakes[0]
        screen.update()

    def extend(self):
        """Increases the length of the snake upon eating"""
        new_x = self.snakes[len(self.snakes) - 1].xcor
        new_y = self.snakes[len(self.snakes) - 1].ycor
        obj = Turtle("square")
        obj.color("white")
        obj.penup()
        obj.speed("slow")
        obj.shapesize(stretch_wid=self.size, stretch_len=self.size)
        obj.goto(new_x, new_y)
        self.snakes.append(obj)

    def move(self):
        """Controls all kind of movements"""
        for i in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[i - 1].xcor()
            new_y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].forward(10)
        screen.onkey(self.left, "Left")
        screen.onkey(self.right, "Right")
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")

    def collision_with_tail(self):
        for snake in self.snakes[1:]:             # Revise later in case forgotten from lec 7 of Day 21(snake game end)
            if snake.distance(self.head) < 5:
                print("Tail")
                return True

    def right(self):
        """Turing_right"""
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def left(self):
        """Turning_left"""
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def down(self):
        """Turning_left"""
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def up(self):
        """Turning_left"""
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
