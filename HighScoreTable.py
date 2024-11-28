class HighScoreTable:

    def __init__(self,length):
        self.length = length
        self.scores_list = []

    def update(self,new_score):
        if len(self.scores_list)<self.length:
            self.scores_list.append(new_score)
            self.scores_list.sort(reverse=True)
        else:
            lowest_score = self.scores_list[-1]
            if new_score > lowest_score:
                self.scores_list.append(new_score)
                self.scores_list.sort(reverse=True)
                self.scores_list.pop()

    @property
    def scores(self):
        return self.scores_list

    def reset(self):
        self.scores_list = []
