
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