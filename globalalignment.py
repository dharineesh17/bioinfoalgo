import numpy as np

seq1 = "ACGGCA"
seq2 = "CAATTGG"
main_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1))

match_checker_matrix = np.zeros((len(seq1) + 1, len(seq2) + 1))

match = 1
mismatch = -1
gap = -2

for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            match_checker_matrix[i][j] = match

        else:
            match_checker_matrix[i][j] = mismatch
# print(match_checker_matrix)

# step 1 initialization
for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            main_matrix[i][0] = i * gap

        else:
            main_matrix[0][j] = j * gap

# step 2 matrix filling

for i in range(1, len(seq1) + 1):
    for j in range(1, len(seq2) + 1):
        main_matrix[i][j] = max(main_matrix[i - 1][j - 1] + match_checker_matrix[i - 1][j - 1],
                                main_matrix[i - 1][j] + gap,
                                main_matrix[i][j - 1] + gap
                                )
# print(main_matrix)

# step 3 Trace back

align1 = ""
align2 = ""

ti = len(seq1)
tj = len(seq2)

while (ti > 0 and tj > 0):

    if (ti > 0 and tj > 0 and main_matrix[ti][tj] == main_matrix[ti - 1][tj - 1] + match_checker_matrix[ti - 1][
        tj - 1]):

        align1 = seq1[ti - 1] + align1
        align2 = seq2[tj - 1] + align2

        ti -= 1
        tj -= 1

    elif (ti > 0 and main_matrix[ti][tj] == main_matrix[ti - 1][tj] + gap):

        align1 = seq1[ti - 1] + align1
        align2 = "_" + align2

        ti -= 1

    else:
        align1 = "_" + align1
        align2 = seq2[tj - 1] + align2

print(align1)
print(align2)