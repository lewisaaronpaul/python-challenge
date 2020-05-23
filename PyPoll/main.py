#################################################################
#Name: Aaron Paul Lewis                                         #
#Rice University: Data Analytics and Visualization Boot Camp    #
#Assignment #3: Python Homework - PyPoll                       #
#Date: May 21, 2020                                             #
#################################################################

#Import the csv module to manage CSV files.
import csv

#Now import the os module to facilitate file paths accross operating systems.
#This allows for portability between different platforms.
import os

#Use Counter from the collection module to give a frequency table of the candidates column.
from collections import Counter

#Link to the relative path of the CSV data file.
election_path = os.path.join('.','Resources', 'election_data.csv')

# Open CSV file and read the CSV file in Dictionary format.
election_open = open(election_path, 'r')
election_reader_dict = csv.DictReader(election_open, delimiter = ',')

# Create the election_data: list of all votes.
#Use list comprehension.
election_data = [row['Candidate'] for row in election_reader_dict]

#Total number of voters.
tot_num_voters = len(election_data)

#Use the Counter from the collections module get a frequency table the votes.
canditates_vote_count = Counter(election_data)

#Print the results of the election.
print("Election Results")
print("-------------------------")
print(f"Total Votes: {tot_num_voters}")
print("-------------------------")

#Results for each candidate:
for name, votes in canditates_vote_count.items():
    print(f"{name}: {(votes * 100 / tot_num_voters):.3f}% ({votes})")

print("-------------------------")

#Identify the winner:
winner = max(canditates_vote_count, key = canditates_vote_count.get)
print(f"Winner: {winner}")
print("-------------------------")

#Create the poll_results.txt file in the Analysis folder, and write the result to it.
results_path = os.path.join('Analysis', 'poll_results.txt')
results_file = open(results_path, 'w')

results_file.write("Election Results \n")
results_file.write("------------------------- \n")
results_file.write(f"Total Votes: {tot_num_voters} \n")
results_file.write("------------------------- \n")

#Write elections results to file.
for name, votes in canditates_vote_count.items():
    results_file.write(f"{name}: {(votes * 100 / tot_num_voters):.3f}% ({votes}) \n")

results_file.write("------------------------- \n")

#Write the winner to file.
results_file.write(f"Winner: {winner} \n")
results_file.write("------------------------- \n")
results_file.close
