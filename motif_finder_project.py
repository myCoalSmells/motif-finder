#importing libraries

import re, csv
from Bio import SeqIO

# FindMotif; Function that finds the inputted motif within the protein sequences in the FASTA file
def FindMotif(motif,seq):

    # Clean the motif using regex.
    motif_clean = re.sub("X", "\\\w", motif)
    motif_clean = re.sub("x", "\\\w", motif_clean)
    motif_clean = re.sub("-", "", motif_clean)
    motif_clean = re.sub("\n", "", motif_clean) 
    needle = re.compile(str(motif_clean))   
    if needle.findall(seq):
        group_matches=[]
        position_matches=[] 
        for match in needle.finditer(seq):
            group_matches.append(match.group(0))
            position_matches.append(match.start(0)+1) 
        return (group_matches, position_matches, len(group_matches))
    else:
        return (["NA"],["NA"],0) 


# Preparing the FASTA file as a CSV file
def FastatoCSV (fasta_file):
    # Open the FASTA file
    handle = open(fasta_file, "r")

    # Open a new, blank CSV file called 'motif search results.csv' and write in its header
    with open ("motif search results.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        header = ['Protein ID', 'Motifs', 'Positions', 'Number of Matches']
        writer.writerow(header)
    
        # use the FindMotif function to search for motifs in a handle,
        # then open CSV file to write in the results
        for record in SeqIO.parse(handle, "fasta"):
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
            motif_row = FindMotif(motif_input, str(record.seq))
            for i in range(0,motif_row[2]):
                spamwriter.writerow([record.id, motif_row[0][i], motif_row[1][i], motif_row[2]])

        csvfile.close()
    
    print("Done!")

# User input
motif_input = input("Input the motif:")


# Input the FASTA file with the sequences.
# It must be in the same folder of your Python Script.
fasta_input = input("Input the FASTA file name:")

# Runs the FastatoCSV function using the inputted FASTA file (fasta_input)
# It will search for the inputted motif (motif_input)
FastatoCSV(fasta_input)

# If your code ran, you should see a file called `motif search results.csv` in your the same folder as your Python notebook. Be sure to open the file and check it to see that the output is what you expected.

