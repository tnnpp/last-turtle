import random
import turtle
from scores import Score
from player import Player
from enemy import Enemy
from bullet import Bullet
from static_score import Static_score


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

start = input("Start game or not: ")
if start == "yes":
    print("game…starting")
    game_is_on = True
    screen = turtle.Screen()
    screen.title("Last turtle")
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
        enemy = Enemy(start_point=start_point,atk=5, hp=1, player=player)
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
game_over.hideturtle()
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


