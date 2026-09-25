from Bio import SeqIO

print("Biopython is working")
from Bio import SeqIO
record=SeqIO. read("Sequence.fasta","fasta")
print("Sequence ID:",record.id)
print("Sequence length:", len(record. seq))
gc_content=((record.seq.count('G')+record.seq.count('C'))/len(record.seq))*100
print("GC_content:",round(gc_content, 2),"%")
print("A:", record.seq.count('A'))
print("C:", record.seq.count('C'))
print("G:", record.seq.count('G'))
print("T:", record.seq.count('T'))