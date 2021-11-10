from turtle import Turtle

#STARTING_POSITIONS = [(-780, 20), (-780, 0), (-780, -20)]

class Paddle(Turtle):

    def __init__(self, position): #coords from main.py goto
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        #self.goto(350, 0)
        self.goto(position)

    # def create_paddle(self):
    #     for i in STARTING_POSITIONS:
    #         new_segment = Turtle("square")
    #         new_segment.color("white")
    #         new_segment.penup()
    #         new_segment.goto(i)
    #         self.segments.append(new_segment)


    def move(self):
        pass

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
