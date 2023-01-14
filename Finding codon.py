# python 3.7.1
# Find the start and stop codon, the TATTAA box, CAAT box, and poly-A tail from the given sequence.

# Author : Dharineesh K S
# Regno  : 123013012

sequence = "5'TAGTTATTAATAGTAATCAATTACGGACCGATATCAGCTGCAATAAACAAGTTCATGATATCCACTGCATTCTAGTTGTGGGCTATGAACTAATGACCCCGTAATTGGGAGAGGAGAGTGTGTCGGGGCGGAGAAGATCTCGAAGTCTTTGTAGCTGGACCTGGGCCTGGGAGCCAGCGAGCTGTGGAGATGTCGGTGGTGGGCATAGACATCAATGTCCATCTCAGGAAGCATGCCGCCCAAAACCCCCCGAAAAACGGCCAGCATGGATACCTCAAACAAGGAAGAGAAA3'"
seq = ''.join(i for i in sequence if i.isupper())


mrna = seq  . replace("T","U") # converting dna to rna 

codons = ['UGA','UAA','UAG',"AUG"]
UAA1 = []
UAG1 = []
UGA1 = []
AUG1 = []
for i in codons:
    if "UGA" == i:
        for j in range(0,len(mrna)):
            if mrna[j:j+len(i)] == i:
                UGA1.append(j+1)
        print(""+i+" stop codon occurred at ",UGA1,"positions")
        print("Total occurrences of "+i+" stop codon is ",len(UGA1))
    elif "UAA" == i:
        for j in range(0,len(mrna)):
            if mrna[j:j+len(i)] == i:
                UAA1.append(j+1)
        print (""+i+" stop codon occurred at ",UAA1,"positions") 
        print("Total occurrences of "+i+" stop codon is ",len(UAA1))
    elif "AUG" == i:
        for j in range(0,len(mrna)):
            if mrna[j:j+len(i)] == i:
                AUG1.append(j+1)
        print(""+i+" start codon occurred at ",AUG1,"positions")
        print("Total occurrences of "+i+" stop codon is ",len(AUG1))
    elif "UAG" == i:
        for j in range(0,len(mrna)):
            if mrna[j:j+len(i)] == i:
                UAG1.append(j+1)
        print(""+i+" stop codon occurred at ",UAG1,"positions")
        print("Total occurrences of "+i+" stop codon is ",len(UAG1))
        
Box = ['TATTAA' , 'CAAT' ]
b0 = []
b1 = []

for x in Box:
    if Box[0] == x:
        for y in range(0,len(seq)):
            if seq[y:y+len(x)] == x:
                b0.append(y+1)
        print(""+x+" box occurred at ",b0,"positions")
    else:
        for y in range(0,len(seq)):
            if seq[y:y+len(x)] == x:
                b1.append(y+1)
        print(""+x+" box occurred at ",b1,"positions")

import re
poly_A = r"[AUCG](A){4,}"

match = re.finditer(poly_A,mrna)
position = []
for m in match:
    pos = m.start()
    position.append(pos+1)
print("PolyA tail region found at ",position)
