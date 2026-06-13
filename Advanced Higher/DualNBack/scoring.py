class Score:
    def __init__(self):
        self.correct = 0
        self.wrong = 0
    def addCorrect(self):
        self.correct +=1
    def addWrong(self):
        self.wrong +=1
    def accuracy(self):
        accuracy = round(((self.correct)/(self.correct + self.wrong) * 100), 2)
        return(accuracy)
    
        
