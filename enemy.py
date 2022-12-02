import turtle
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

