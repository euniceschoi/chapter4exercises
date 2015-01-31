#open genomic dna file and read it
genomic_dna = open("genomic_dna.txt").read()

#open exons file
exon_locations = open("exons.txt")

#create a variable to hold coding sequence
coding_sequence = ""

#go through each line in exons locations file
for line in exon_locations:

	#split the lines
	positions = line.split(',')
	
	#get start and stop positions
	start = int(positions[0])
	stop = int(positions[1])

	#extract the exon from the genomic dna
	exon = genomic_dna[start:stop]
	
	#append the exon to the end of current coding sequence
	coding_sequence = coding_sequence + exon

# write the coding sequence to an output file
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
#always close 
