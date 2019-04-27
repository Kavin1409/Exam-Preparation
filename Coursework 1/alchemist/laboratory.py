import random
from pytest import raises
import yaml


class Laboratory:

    def __init__(self, filename):
        self.filename = filename
        self.shelf1 = filename['lower']
        self.shelf2 = filename['upper']

        if len(self.filename.keys()) != 2:
            raise TypeError(
                "Only 2 shelves are accepted")

        for i in self.shelf1:
            if type(i) == int or type(i) == float:
                raise ValueError(
                    i, " in the lower shelf is not an acceptable name")
        for i in self.shelf2:
            if type(i) == int or type(i) == float:
                raise ValueError(
                    i, " in the upper shelf is not an acceptable name")

    def can_react(self, substance1, substance2):
        return (substance1 == "anti" + substance2) or (substance2 == "anti"
                                                       + substance1)

    def update_shelves(self, shelf1, shelf2, substance1, substance2_index):
        index1 = shelf1.index(substance1)
        shelf1 = shelf1[:index1] + shelf1[index1+1:]
        shelf2 = shelf2[:substance2_index] + shelf2[substance2_index+1:]
        return shelf1, shelf2

    def do_a_reaction(self, shelf1=None, shelf2=None):
        for substance1 in shelf1:
            possible_targets = [i for i, target in enumerate(shelf2) if
                                self.can_react(substance1, target)]
            if not possible_targets:
                continue
            else:
                substance2_index = random.choice(possible_targets)
                return self.update_shelves(shelf1, shelf2,
                                           substance1, substance2_index)
        return shelf1, shelf2

    def run_full_experiment(self, reaction=None):
        count = 0
        ended = False
        shelf1 = self.shelf1
        shelf2 = self.shelf2

        if len(shelf1) == 0:
            print("Your lower shelf is empty!")
        if len(shelf2) == 0:
            print("Your upper shelf is empty!")

        while not ended:
            shelf1_new, shelf2_new = self.do_a_reaction(shelf1, shelf2)
            if shelf1_new != shelf1:
                count += 1
            ended = (shelf1_new == shelf1) and (shelf2_new == shelf2)
            shelf1, shelf2 = shelf1_new, shelf2_new
        return shelf1, shelf2, count

    def total_reactions(self):
        k1, k2, k3 = self.run_full_experiment()
        results = dict(
            lower=k1,
            upper=k2
        )
        print(yaml.safe_dump(results, default_flow_style=False))

    def print_reaction_number(self):
        k1, k2, k3 = self.run_full_experiment()
        print(k3)
        return k3
