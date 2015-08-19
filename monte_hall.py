

import random

GOAT = 'goat'
CAR = 'car'

class Game(object):

    def __init__(self):
        self.guess = None
        self.revealed_goat = None

        # begin with an array of three things, a random one of which is a car
        self.doors = [GOAT, GOAT, GOAT]
        car = random.choice(range(len(self.doors)))
        self.doors[car] = CAR

    def make_guess(self, n=None):
        # set self.guess to the index guessed, or a random index by default
        if n is None:
            n = random.choice(range(len(self.doors)))
        self.guess = n

    def reveal_goat(self):
        # set self.revealed_goat to a random index among the ones not yet chosen

        # sanity checking
        assert self.guess is not None
        assert CAR in self.doors

        # begin with all options available
        options = set(range(len(self.doors)))
        # but remove the chosen door
        options.discard(self.guess)
        # then remove the car
        for i, prize in enumerate(self.doors):
            if prize == CAR:
                options.discard(i)

        # legal options are all remaining goat doors
        for i in options:
            assert self.doors[i] == GOAT

        # reveal a random legal option
        self.revealed_goat = options.pop()
        return self.revealed_goat

    def switch(self):
        # set self.guess to the other door that was not initially guessed and was not revealed as a goat

        assert self.guess is not None
        assert self.revealed_goat is not None

        options = set(range(len(self.doors))) - set([self.guess, self.revealed_goat])

        assert len(options) == 1

        self.guess = options.pop()

    def did_win(self):
        return self.doors[self.guess] == CAR



class Simulation(object):

    SWITCH = 'switch'
    KEEP = 'keep'

    def __init__(self, num_runs, strategy, guess=None):
        self.num_runs = num_runs
        self.num_correct = 0
        self.strategy = strategy
        if guess is None:
            guess = random.randint(0, 2)
        self.guess = guess

    def run(self):
        for _ in range(self.num_runs):
            g = Game()
            g.make_guess(self.guess)
            g.reveal_goat()
            if self.strategy == Simulation.SWITCH:
                g.switch()
            won = g.did_win()
            if won:
                self.num_correct += 1
        return (self.num_runs, self.num_correct)


