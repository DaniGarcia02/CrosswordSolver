class Gap:
    def __init__(self, id, word, position):
        self.id = id
        self.word = word
        self.position = position
        self.intersections = []
        self.possible_words = []
        self.n_possible_words = 0