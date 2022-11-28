import random
import time
import turtle
import math
screen = turtle.Screen()
screen.setup(width=600, height=600)

class Score:
    def __init__(self,score=0, score_player_cal=0, score_enemy_cal=0):
        self.__score = score
        self.__score_player_cal = score_player_cal
        self.__score_enemy_cal = score_enemy_cal
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,score):
        if not isinstance(score, int):
            raise TypeError("score must be int")
        self.__score = score

    @property
    def score_player_cal(self):
        return self.__score_player_cal
    @score_player_cal.setter
    def score_player_cal(self, score):
        if not isinstance(score,(int)):
            raise TypeError("score_player must be int")
        self.__score_player_cal = score
        if self.__score_player_cal == 250 :
            self.__score_player_cal = 0
    @property
    def score_enemy_cal(self):
        return self.__score_enemy_cal
    @score_enemy_cal.setter
    def score_enemy_cal(self,score):
        if not isinstance(score,(int)):
            raise TypeError("score_enemy must be int")
        self.__score_enemy_cal = score
        if self.__score_enemy_cal == 600:
            self.__score_enemy_cal = 0



class Player(turtle.Turtle):
    """ Define Player and plyer stat"""
    def __init__(self, atk=5 ,level=0, hp=45):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("green")
        self.setheading(0)
        self.penup()
        self.level = level
        self.hp = hp
        self.atk = atk

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,level):
        if not isinstance(level, int):
            raise TypeError("level must be int")
        self.__level = level

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, hp):
        if not isinstance(hp, int):
            raise TypeError("hp must be int")
        self.__hp = hp


    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self, atk):
        if not isinstance(atk, (int, float)):
            raise TypeError("atk must be number")
        self.__atk = atk


    def cal_stat(self,score):
        if score.score_player_cal == 0:
            self.level = self.level +1
            self.hp = self.hp + 5
            self.atk = self.atk + 0.25

    def move_right(self):
        # self.setheading(0)
        # self.forward(5)
        self.right(45)
    def move_up(self):
        # self.setheading(90)
        self.forward(5)

    def move_down(self):
        # self.setheading(270)
        # self.forward(5)
        self.backward(5)

    def move_left(self):
        # self.setheading(180)
        # self.forward(5)
        self.left(45)
    def get_coordinate(self):
        return self.xcor(),self.ycor()

    def enemy_hit(self,enemy):
        for i in enemy:
            if self.distance(i) < 35:
                self.hp = self.hp - enemy.atk


class Enemy(turtle.Turtle):
    """ Defind enemy object and stat"""
    def __init__(self,start_point=None,atk=4 ,level=0, hp=1 ,player=0):
        turtle.Turtle.__init__(self, visible=False)
        self.shape("turtle")
        self.color("red")
        init_speed = self.speed()
        self.speed(0)
        self.penup()
        self.setx(start_point[0][0])
        self.sety(start_point[0][1])
        self.speed(init_speed)
        self.showturtle()
        self.level = level
        self.hp = hp
        self.atk = atk
        self.player = player

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self,level):
        if not isinstance(level, int):
            raise TypeError("level must be int")
        self.__level = level

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, hp):
        if not isinstance(hp, int):
            raise TypeError("hp must be int")
        self.__hp = hp


    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self, atk):
        if not isinstance(atk, (int, float)):
            raise TypeError("atk must be number")
        self.__atk = atk




    def move_to_player(self,all_enemy):
        for enemy in all_enemy:
            enemy.speed("fastest")
            enemy.setheading(enemy.towards(self.player))
            enemy.forward(10)
        # screen.ontimer(self.move_to_player, 1)

    def bullet_hit(self,bullets):
        for enemy in self.all_enemy:
            if enemy.distance(bullets) < 35 :
                self.hp = self.hp - self.player.atk
            if self.hp == 0:
                enemy.hideturtle()
                bullets.hideturtle()


class Bullet(turtle.Turtle):
    def __init__(self,player,state,all_enemy):
        self.player = player
        turtle.Turtle.__init__(self,shape="arrow",visible=False)
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
        while -600 < x < 600 and -600 < y< 600 and self.state == True :
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
                i.hideturtle()
                self.all_enemy.remove(i)

        return self.state







class UIdisplay:
    def __init__(self,data):
        self.data = data
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data
    def show_level(self):
        pass




player = Player()
score = Score()
# player_dict = {'hp':player.hp, 'level': player.level, 'score': player.score }





screen.listen()
# setup key
screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_up,key='w')
screen.onkeypress(fun=player.move_down,key='s')
screen.onkeypress(fun=player.move_left,key='a')
all_bullet = []
all_enemy = []
# run game
game_is_on = True
while game_is_on:
    screen.update()
    # create enemy

    if len(all_enemy) < 10 :
        start_point = [[0, 200], [600, 0], [0, -200], [-600, 0]]
        random.shuffle(start_point)
        enemy = Enemy(start_point=start_point,atk=4, level=0, hp=1, player=player)
        all_enemy.append(enemy)
    enemy.move_to_player(all_enemy)

    # create bullet
    bullet = Bullet(player, True,all_enemy)
    screen.onkey(fun=bullet.move, key='Return')
    all_bullet.append(bullet)



