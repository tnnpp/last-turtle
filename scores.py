class Score:
    def __init__(self,score=0, score_player_cal=0):
        self.__score = score
        self.__score_player_cal = score_player_cal

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
