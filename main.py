import random
import time
import turtle
import math

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
    def __init__(self, atk=5 ,level=1, hp=50):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.level = level
        self.hp = hp
        self.atk = atk
        self.max_hp = hp

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


    def cal_stat(self,score,uidisplay):
        if score.score_player_cal == 0 and score.score != 0:
            score.score_player_cal = 25
            uidisplay.show_level_list[0].clear()
            uidisplay.show_hp_list[0].clear()
            del uidisplay.show_hp_list[0]
            del uidisplay.show_level_list[0]
            self.level = self.level + 1
            self.max_hp += 5
            self.hp = self.max_hp + 5
            self.atk = self.atk + 0.25
            uidisplay.show_hp()
            uidisplay.show_level()


    def move_right(self):
        self.right(45)

    def move_up(self):
        self.forward(5)

    def move_down(self):
        self.backward(5)

    def move_left(self):
        self.left(45)

    def get_coordinate(self):
        return self.xcor(),self.ycor()

    def enemy_hit(self,enemy,uidisplay):
        state = True
        for i in enemy:
            if self.distance(i) < 35:
                uidisplay.show_hp_list[0].clear()
                del uidisplay.show_hp_list[0]
                self.hp = self.hp - i.atk
                uidisplay.show_hp()
                uidisplay.show_level()
                if self.hp <= 0 :
                    state = False
        return state

class Enemy(turtle.Turtle):
    """ Defind enemy object and stat"""
    def __init__(self,start_point=None,atk=5 ,level=0, hp=1 ,player=0):
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
            enemy.forward(50)
        # screen.ontimer(self.move_to_player, 1)




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
                    self.score.score_enemy_cal += 25

        return self.state

class UIdisplay:
    def __init__(self, player, all_enemy, score):
        self.player = player
        self.all_enemy = all_enemy
        self.score = score
        self.__show_score_list = []
        self.__show_hp_list = []
        self.__show_level_list = []
        self.name = "none"

    @property
    def show_score_list(self):
        return self.__show_score_list

    @property
    def show_hp_list(self):
        return self.__show_hp_list

    @property
    def show_level_list(self):
        return self.__show_level_list

    def show_score(self):
        p_score = turtle.Turtle()
        p_score.up()
        p_score.hideturtle()
        p_score.color('black')
        p_score.goto(-550, 275)
        p_score.write(f'Score: {score.score}', font=('Bahnschrift SemiLight SemiConde', 24, 'normal'))
        self.show_score_list.append(p_score)

    def show_hp(self):
        p_hp = turtle
        p_hp.up()
        p_hp.hideturtle()
        p_hp.color('black')
        p_hp.goto(-410, 275)
        p_hp.write(f'HP: {player.hp}', font=('Bahnschrift SemiLight SemiConde', 24, 'normal'))
        self.show_hp_list.append(p_hp)

    def show_level(self):
        p_level = turtle
        p_level.up()
        p_level.hideturtle()
        p_level.color('black')
        p_level.goto(-300, 275)
        p_level.write(f'Level: {player.level}', font=('Bahnschrift SemiLight SemiConde', 24, 'normal'))
        self.show_level_list.append(p_level)

    def name_showing(self):
        self.name = screen.textinput('make your decision', 'What is your name')
        name_show = turtle.Turtle()
        name_show.up()
        name_show.hideturtle()
        name_show.color('black')
        name_show.goto(-550, 230)
        name_show.write(f'Name: {self.name}', font=('Bahnschrift SemiLight SemiConde', 24, 'normal'))
        return name_show

class Static_score:
    def __init__(self, score, uidisplay, player):
        self.score = score
        self.uidisplay = uidisplay
        self.player = player

    def write(self):
        try:
            with open('data.txt', "r") as data_file:
                data = data_file.read()

        except FileNotFoundError:
            with open('data.txt', "w") as data_file:
                data = data_file.write()
        else:
            with open('data.txt', "w") as data_file:
                data_file.write(f"{data}\nname: {self.uidisplay.name}, level: {self.player.level}, score:{self.score.score}")
    def read(self):
        with open('data.txt', "r") as data_file:
            data = data_file.read()
            data.splitlines()
        return data

start = input("Start game or not: ")
if start == "yes":
    print("game…starting")
    game_is_on = True
    screen = turtle.Screen()
else:
    game_is_on = False
    print("game don't start")

all_bullet = []
all_enemy = []

# set up class
player = Player()
score = Score()
display = UIdisplay(player,all_enemy,score)
static = Static_score(score, display, player)

name_show = display.name_showing()


screen.listen()
# setup key
screen.onkeypress(fun=player.move_right, key='d')
screen.onkeypress(fun=player.move_up,key='w')
screen.onkeypress(fun=player.move_down,key='s')
screen.onkeypress(fun=player.move_left,key='a')

# displaystat
display.show_score()
display.show_hp()
display.show_level()

# run game

while game_is_on:
    screen.update()
    # create enemy
    if len(all_enemy) < 10 :
        start_point = [[0, 300], [600, 0], [0, -300], [-600, 0]]
        random.shuffle(start_point)
        enemy = Enemy(start_point=start_point,atk=4, level=0, hp=1, player=player)
        all_enemy.append(enemy)
    enemy.move_to_player(all_enemy)

    # create bullet
    bullet = Bullet(player, True, all_enemy, score, display)
    screen.onkey(fun=bullet.move, key='Return')
    all_bullet.append(bullet)

    player.cal_stat(score,display)

    game_is_on = player.enemy_hit(all_enemy,display)


static.write()
for i in all_enemy:
    i.hideturtle()
player.hideturtle()
for i in display.show_hp_list:
    i.clear()
for i in display.show_level_list:
    i.clear()
for i in display.show_score_list:
    i.clear()
for i in all_bullet:
    i.hideturtle()
name_show.clear()
game_over = turtle.Turtle()
game_over.write('GAME OVER', align='center',font=('Engravers MT', 50, 'normal'))
your_score = turtle.Turtle()
your_score.hideturtle()
your_score.penup()
your_score.goto(0,-50)
your_score.write(f'your statistic name:{display.name}, level: {player.level}, score: {score.score}', align='center',font=('Bahnschrift SemiLight SemiConde', 24, 'normal'))

data = static.read()

# for i in range(len(data)):
#     print(f'#{i} {data[i]}')
print("GAME OVER")
print("===================================")
print("History")
print(data)

screen.exitonclick()


