from Bio import SeqIO
from pathlib import Path

# Input FASTA file
fasta_file = Path("Sequence.fasta")

if not fasta_file.exists():
    raise FileNotFoundError(
        "Sequence.fasta not found. Check the file location."
    )

# Read the FASTA sequence
record = SeqIO.read(str(fasta_file), "fasta")
sequence = str(record.seq).upper()

if not sequence:
    raise ValueError("The FASTA sequence is empty.")

# Calculate sequence statistics
sequence_length = len(sequence)
a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content = ((g_count + c_count) / sequence_length) * 100

other_bases = sequence_length - (
    a_count + t_count + g_count + c_count
)

# Display results
print("DNA FASTA Sequence Analysis")
print("-" * 30)
print("Sequence ID:", record.id)
print("Sequence length:", sequence_length, "bp")
print("GC content:", round(gc_content, 2), "%")
print("A:", a_count)
print("T:", t_count)
print("G:", g_count)
print("C:", c_count)
print("Other/ambiguous bases:", other_bases)
