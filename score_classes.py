class Football:
    def __init__(self,team_name):
        """
        This function creates the class for a football team, setting the score at zero and giving it a name.
        :param team_name: This is
        """
        self.team_name = team_name
        self.score = 0
    def safety(self):
        self.score += 2
    def field_goal(self):
        self.score += 3
    def touchdown(self):
        self.score += 6
    def extra_point(self):
        self.score += 1
    def two_point_conversion(self):
        self.score += 2
    def reset(self):
        self.score = 0


class Basketball:
    def __init__(self,team_name):
        self.team_name = team_name
        self.score = 0
    def two_point(self):
        self.score += 2
    def three_point(self):
        self.score += 3
    def free_throw(self):
        self. score += 1

    def reset(self):
        self.score = 0

class Baseball:
    def __init__(self,team_name):
        self.team_name = team_name
        self.score = 0
    def run(self):
        self.score += 1
    def grand_slam(self):
        self.score += 4

    def reset(self):
        self.score = 0

class Hockey:
    def __init__(self,team_name):
        self.team_name = team_name
        self.score = 0
    def goal(self):
        self.score += 1
    def reset(self):
        self.score = 0
