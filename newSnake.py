class newSnake():
    # TODO: mimic github snake, express it in python.

    def __init__(self):
        self.score = 1
        self.remainingMoves = 200
        self.lifeTimes = 0  # Amount of time the snake is alvie.
        self.fitness = 0
        self.dead = False
        self.replay = False
        self.vision = []
        self.decision = []
        self.head
        self.body = []
        self.foodList = []  # store food locations to replay the game
        self.Food
        self.brain
