import random
import copy

class Hat :
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        for i, j in self.balls.items():
            for x in range(j):
                self.contents.append(i) 
    
    def draw(self, nbr_balls):
        if len(self.contents) > nbr_balls:
            self.new_contents = random.sample(self.contents, k=nbr_balls)
            for i in self.new_contents :
                self.contents.remove(i)
            return self.new_contents
        else :
            return self.contents


def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    count = 0
    for i in range(num_balls_drawn):
        expected_copied = copy.deepcopy(expected_balls)
        hat_copied = copy.deepcopy(hat)
        colors_drawn = hat_copied.draw(num_balls_drawn)         
        for color in colors_drawn:
            if (color in expected_copied):
                expected_copied[color]-=1

        if (all(x <= 0 for x in expected_copied.values())):
            count += 1
    return count / num_experiments
                

