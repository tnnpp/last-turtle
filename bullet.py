import turtle
class Bullet(turtle.Turtle):
    def __init__(self,player,state,all_enemy,score,uidisplay):
        self.player = player
        turtle.Turtle.__init__(self, shape="arrow", visible=False)
        self.shapesize(0.1, 0.75, 0.1)
        self.color("black")
        init_speed = self.speed()
        self.speed(0)
        self.penup()
        self.setx(1000)
        self.sety(1000)
        self.speed(init_speed)
        self.state =state
        self.all_enemy = all_enemy
        self.score = score
        self.uidisplay = uidisplay

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self,state):
        self.__state = state


    def move(self):
        x, y = self.player.get_coordinate()
        init_speed = self.speed()
        self.speed(0)
        self.setx(x)
        self.sety(y)
        self.speed(init_speed)
        x = self.xcor()
        y = self.ycor()
        self.setheading(self.player.heading())
        self.showturtle()
        while -600 < x < 600 and -300 < y < 300 and self.state == True :
            x = self.xcor()
            y = self.ycor()
            # self.bullet_hit()
            # self.speed()
            self.forward(50)
            self.bullet_hit()
        self.hideturtle()

    def bullet_hit(self):
        self.state = True
        for i in self.all_enemy:
            if self.distance(i) < 35:
                self.state = False
                i.hp = 0
                # i.hp = i.hp - self.player.atk
                if i.hp == 0:
                    i.hideturtle()
                    i.goto(1000,1000)
                    self.all_enemy.remove(i)
                    self.uidisplay.show_score_list[0].clear()
                    del self.uidisplay.show_score_list[0]
                    self.score.score = self.score.score + 25
                    self.uidisplay.show_score()
                    self.score.score_player_cal += 25

        return self.state