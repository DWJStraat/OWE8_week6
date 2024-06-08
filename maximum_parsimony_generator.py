from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import *
from Bio.Phylo import NewickIO
import matplotlib

with open(input("Enter the file path to a MSA alignment:\n") as f:
    alignment = AlignIO.read(f, "clustal")

scorer = ParsimonyScorer()
searcher = NNITreeSearcher(scorer= scorer)
constructor = ParsimonyTreeConstructor(searcher)
pars_tree = constructor.build_tree(alignment)
with open("newick.txt", 'w') as f:
    trees = [pars_tree]
    NewickIO.write(trees, f)
