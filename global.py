# Implementation of Global alignment using Biopython

from Bio import pairwise2

from Bio.Align import substitution_matrices

blosum62 = substitution_matrices.load("BLOSUM62")

seq1 = "SHMQTPETAFINNVTSNGGYHSWHLVSGDLIVKDVCYKKLLHWSGQTICYADNKFYVVKNDVALPFSDLEA"

seq2 = "LQGCDEFIVPLCVFNGHSRGSSSDPANTYYMDSQMYYNTVTGVFYGFNSTLDVGTTVQNPGLDLTCSYLAL"

alignments = pairwise2.align.globalds(seq1, seq2, blosum62, -10, -0.5 )

print("Global alignment")

print(pairwise2.format_alignment(*alignments[0]))