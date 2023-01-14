# CONSTRUCT AN HMM VITERBI ALGORITHM TO IDENTIFY GC RICH REGIONS IN THE GIVEN SEQUENCE (S="GGCA).

import random
import math
import numpy

def rand_multinomial (probs):
    assert(abs(sum(probs) - 1.0) < le-5)
    rand = random.random()
    for index, prob in enumerate(probs):
        if rand <prob:
            return index
        else:
            rand -= prob
    return 0

def rand_multinomial_iter(iterator):
    rand = random.random()
    for key, prob in iterator:
        if rand <prob:
            return key
        else:
            rand -= prob
    return 0

class HMM():
    def _init_(self):
        self.num_states = 2
        self.prior = [0.5, 0.5]
        self.transition = [[0.999, 0.001], [0.01, 0.99]]
        self.emission = [{"A": 0.291, "T": 0.291, "C": 0.209, "G": 0.209}, #L
                     {"A": 0.169, "T": 0.169, "C": 0.331, "G": 0.331}] #H
        sequence = []
        states = []
        rand = random.random()
        cur_state= rand_multinomial(self.prior)
        for i in range(length):
            states.append(cur_state)
            char = rand_multinomial_iter(self.emission[cur_state].items())
            sequence.append(char)
            cur_state = rand_multinomial(self.transition[cur_state])
            return sequence, states
    def generate_sequence(self, states):
       sequence = []
       for state in states:
           char = rand_multinomial_iter(self.emission[state].items())
           sequence.append(char)
       return sequence
    def logprob(self, sequence, states):
      result = []
      initial = self.emission[states[0]][sequence[0]]
      result.append(math.log(self.prior[0]) + math.log(initial))
      for i in range(1, len(sequence)):
          em = self.emission[states[i]] [sequence[i]]
          trns = self.transition[states[i-1]][states[i]]
          prev = result[i-1]
          result.append(math.log(trns) + math.log(em) + prev)
      return result[len (result)-1]
    def viterbi(self, sequence):
      l = len(sequence)
      initial0 = self.emission[0][sequence[0]]
      initiall= self.emission[1][sequence[0]]
      row0 = numpy.empty([self.num_states, l])
      row1 = numpy.empty([self.num_states, l])
      row0[0, 0] = math.log(self.prior[0]) + math.log(initial0)
      row0[1, 0] = math.log(self.prior[1])+ math.log(initiall)
      row1[0, 0] = 0
      row1[1, 0] = 0
      for i in range(1, 1):
          for j in range(0, self.num_states):
               prev1 = row0[0][i-1]
               prev2 = row0[1][i-1]
               emission = self.emission[j][sequence[i]]
               trnsl= self.transition[0][j]
               trns2 = self.transition[1][j]
               low = math.log(trnsl) + prevl
               high = math.log(trns2) + prev2
               row0[j,i] = max(low, high) + math.log(emission)
               row1[j,i] = numpy.argmax([low, high])
          states = numpy.empty(l, int)
          states[l-1] = rowO[:, 1-1].argmax()
          for j in range(1-1, 0, -1):
              states[j-1] = row1[states[j],j]
          return states.tolist()
    def read_sequence(filename):
        with open(filename, "r") as f:
            return f.read().strip()
    def write_sequence(filename, sequence):
        with open(filename, "w") as f:
            f.write("".join(sequence))
    def write_output (filename, logprob, states):
        with open(filename, "w") as f:
            f.write(repr(logprob))
            f.write("\n")
            for state in range(2):
                f.write(str(states.count(state)))
                f.write("\n")
                f.write("".join(map(str, states)))
                f.write("\n")

hmm = HMM()

with open
sequence= read_sequence("small.txt")
viterbi = hmm.viterbi(sequence)
logprob = hmm.logprob(sequence, viterbi)
write_output("my_small_output.txt", logprob, viterbi)