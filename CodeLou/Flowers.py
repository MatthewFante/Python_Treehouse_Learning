# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input 
# file and prints the information to the user's screen. 
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file
theFile = open("flowers.dat", 'r').readlines()
theLines = [line.rstrip('\n') for line in theFile]

counter = 0

while counter < len(theLines): 
    print(theLines[counter], "grows in the", theLines[counter + 1])
    counter += 2

