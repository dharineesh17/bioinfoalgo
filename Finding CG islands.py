# python 3.7.1
# Finding the positions and the total occurrences of CG-islands in the genomic sequence

# Author : Dharineesh K S
# Regno  : 123013012
import re

seq = input("Enter DNA sequences in upper case")

a = re.search("[^ATCG]",seq)
if a:
    print("Ambiguous bases found!")
    seq = input("Reenter your DNA sequence now")


rgx = re.compile("CG")
i=1
pos = []
for mo in rgx.finditer(seq):
    startpos=(mo.start())
    pos.append(startpos+1)
    i += 1
tot = i-1
print("CG-islands found at ",pos)
print("Total occurrences of CG-islands is ", tot)