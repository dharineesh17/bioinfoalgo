from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
msa = AlignIO.read(open('seq.phy'), 'phylip')
print(msa)
constructor = DistanceTreeConstructor()
calculator = DistanceCalculator('identity')
dist_matrix = calculator.get_distance(msa)
upgma_tree = constructor.upgma(dist_matrix)
print(upgma_tree)

nj_tree = constructor.nj(dist_matrix)
print(nj_tree)