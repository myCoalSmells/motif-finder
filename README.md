# motif-finder

Originally made in Jupyter Notebook.

This program gives Python some protein sequences in a FASTA file, asking the user for an amino acid sequence (single-letter), then using regular expressions to search for the amino acid pattern within the FASTA sequences.

The FindMotif function uses regular expressions to search for a short motif pattern within a larger sequence of characters (in this case, an one-letter amino acid sequence).
The FastatoCSV does three things at once: open the data file containing a FASTA sequence, and use the FindMotif function to write the results to a CSV file.
