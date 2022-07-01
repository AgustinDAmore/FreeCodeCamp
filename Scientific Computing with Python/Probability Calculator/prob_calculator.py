class Hat(object):

    __slots__ = ['contents',"list_of_contents"]

    def __init__ (self, **contents):
        self.contents = contents
        self.list_of_contents = []
        for key, value in self.contents.items():
            for i in range(value):
                self.list_of_contents.append(key)
        
    def draw(self, n):
        import random
        n = min(n, len(self.list_of_contents))
        eliminated = []
        for i in range(n):
            result = random.randrange(0,len(self.list_of_contents))
            eliminated.append(self.list_of_contents.pop(result))
            
        return eliminated

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hitCunter = 0
    import copy
    for _ in range(num_experiments):
        newhat = copy.deepcopy(hat)
        balls_drawn = newhat.draw(num_balls_drawn)
        ballsRequired = sum([1 for i, j in expected_balls.items() if balls_drawn.count(i) >= j])
        if ballsRequired == len(expected_balls):
            hitCunter += 1

    return hitCunter / num_experiments 

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
    expected_balls={"red":2,"green":1}, 
    num_balls_drawn=5, 
    num_experiments=2000)

print("the probability is: ",probability,"%")