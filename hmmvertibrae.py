import sys
import random
import math
from math import log


def rand_multinomial(probs):
    assert (abs(sum(probs) - 1.0) < 1e-5)
    rand = random.random()
    for index, prob in enumerate(probs):
        if rand < prob:
            return index
        else:
            rand -= prob
    return 0


def rand_multinomial_iter(iterator):
    rand = random.random()
    for key, prob in iterator:
        if rand < prob:
            return key
        else:
            rand -= prob
    return 0


class HMM():

    def __init__(self):
        self.num_states = 2
        self.prior = [0.5, 0.5]
        self.transition = [[0.999, 0.001], [0.01, 0.99]]
        self.emission = [{"A": 0.291, "T": 0.291, "C": 0.209, "G": 0.209},
                         {"A": 0.169, "T": 0.169, "C": 0.331, "G": 0.331}]
        # Generates a sequence of states and characters from

    # the HMM model.
    # - length: Length of output sequence
    def sample(self, length):
        sequence = []
        states = []
        rand = random.random()
        cur_state = rand_multinomial(self.prior)
        for i in range(length):
            states.append(cur_state)
            char = rand_multinomial_iter(self.emission[cur_state].items
                                         ())
            sequence.append(char)
            cur_state = rand_multinomial(self.transition[cur_state])
        return sequence, states

        # Generates a emission sequence given a sequence of states

    def generate_sequence(self, states):
        sequence = []
        for state in states:
            char = rand_multinomial_iter(self.emission[state].items())
            sequence.append(char)
        return sequence

        # computes log(P(sequence, states))

    def logprob(self, sequence, states):
        num = 1
        finprob = log(0.5) + log(self.emission[states[0]][sequence[0]])

        while num < len(states):
            prob = log(self.transition[states[num -
                                              1]][states[num]]) + log(self.emission[states[num]][sequence[num]])
            num += 1
            finprob += prob

        return finprob

    def viterbi(self, sequence):
        final = []  # result array
        seqlen = len(sequence)  # length of the states sequence
        val = 0
        prior = [[0 for x in range(seqlen)] for y in range(2)]  # prior vals
        probslist = [[0 for x in range(seqlen)] for y in range(2)]
        for y in range(seqlen):  # runs through states
              for x in range(2):  # runs through the 0's and ones
                    if y == 0:
                        probslist[x][y] = log(self.emission[x][sequence[y]]) + log(self.prior[x])
                    else:
                      # updates priors
                        prior0 = log(self.transition[0][x]) + probslist[0][y - 1]
                        prior1 = log(self.transition[1][x]) + probslist[1][y - 1]
                        # checks if its a 1
                        if prior0 < prior1:
                            probslist[x][y] = log(self.emission[x][sequence[y]]) + prior1
                            prior[x][y] = 1
                        else:
                            # checks if its not a 1 then it must be a 0
                            probslist[x][y] = log(self.emission[x][sequence[y]]) + prior0
                            prior[x][y] = 0

        if ((probslist[0][seqlen - 1]) < (probslist[1][seqlen - 1])):
            val = 1

        for x in range(seqlen):
           final.append(val)
           val = prior[val][seqlen - 1 - x]
           final.reverse()
           return final


# End your code
def read_sequence(filename):
    with open(filename, "r") as f:
        return f.read().strip()


def write_sequence(filename, sequence):
    with open(filename, "w") as f:
        f.write("".join(sequence))


def write_output(filename, logprob, states):
    with open(filename, "w") as f:
        f.write(str(logprob))
        f.write("\n")
        for state in range(2):
            f.write(str(states.count(state)))
            f.write("\n")
        f.write("".join(map(str, states)))
        f.write("\n")


hmm = HMM()

file = sys.argv[0]
sequence = read_sequence(file)
viterbi = hmm.viterbi(sequence)
logprob = hmm.logprob(sequence, viterbi)
name = "my_" + file[:-4] + '_output.txt'
write_output(name, logprob, viterbi)