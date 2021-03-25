# Import the correct dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("election-analysis","Resources","election_results.csv")
#Assign variable for the file to write to
file_to_save = os.path.join("election-analysis","analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

 