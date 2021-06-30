class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goal=1):
        self.goals += goal

    def make_assist(self, assist=1):
        self.assists += assist

    def statistics(self):
        print(self.surname + ' ' + self.name + ' - голы: ' + str(self.goals) + ', передачи: ' + str(self.assists))


s = SoccerPlayer('John', 'Иванов')
s.score(5)
s.make_assist(3)
s.statistics()
