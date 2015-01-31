#open file
file = open("input.txt")

#output file
output = open("trimmed.txt", "w")

for dna in file:
	trimmed_dna = dna[14:]
	#this removes first 14 characters
	output.write(trimmed_dna)
	print("processed sequence with length " + str(len(trimmed_dna)))
	#prints out length for each line


