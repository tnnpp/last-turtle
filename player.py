import turtle
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