#!/usr/bin/env python
# coding: utf-8

# Import operating system and CSV packages
import os
import csv

# Declare files paths to CSV and text files
csvpath = "Resources/election_data.csv"
textpath = "Analysis/analysis.txt"

# Open CSV file as read-only with UTF-8 encoding
with open(csvpath, "r", encoding='utf8') as csvfile:
    # Read contents of CSV file into variable
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Bypass header row
    header = next(csvreader)
    
    # Initiate empty lists
    ballot_id = []
    candidate = []
    
    # Loop through rows in CSV file
    for r in csvreader:
        # Append values for each ballot ID to "ballot_id" list
        ballot_id.append(r[0])
        
        # Append unique values for each candidate to "ballot_id" list
        candidate.append(r[2])
        
        # Put profit & loss values into a list as integers
        # plint = [eval(i) for i in pl]
        # Add difference values to "change" list
        # change = [y - x for x, y in zip(plint, plint[1:])]

# Calculate and format number of votes
ballot_count = len(ballot_id)
ballot_format = "{:,}".format(ballot_count)

# Calculate total and percentage, and format votes for each candidate
ccs_count = candidate.count("Charles Casper Stockham")
ccs_format = "{:,}".format(ccs_count)
ccs_percent = (ccs_count / ballot_count)
ccs_performat = "{:.2%}". format(ccs_percent)

dd_count = candidate.count("Diana DeGette")
dd_format = "{:,}".format(dd_count)
dd_percent = (dd_count / ballot_count)
dd_performat = "{:.2%}". format(dd_percent)

rad_count = candidate.count("Raymon Anthony Doane")
rad_format = "{:,}".format(rad_count)
rad_percent = (rad_count / ballot_count)
rad_performat = "{:.2%}". format(rad_percent)

# Initiate and append empty "winner" list with vote counts
winner = []
winner.extend([rad_count, ccs_count, dd_count])

# Initiate empty list of candidate names
unique_candidate = []

# Set list with unique candidate names
unique_candidate = list(set(candidate))

# Zip lists of candidate names and votes together
candidate_dict = dict(zip(unique_candidate, winner))

# Retrieve candidate with the most votes
winner_candidate = max(candidate_dict, key=candidate_dict.get)

# Print values to terminal
print(f"""Election Results
----------------------------
Total Votes: {ballot_format}
----------------------------
Charles Casper Stockham: {ccs_performat} ({ccs_format})
Diana DeGette: {dd_performat} ({dd_format})
Raymon Anthony Doane: {rad_performat} ({rad_format})
----------------------------
Winner: {winner_candidate}""")

# Open and write values to text file
with open(textpath, 'w') as text:
    text.write(f"""Election Results
----------------------------
Total Votes: {ballot_format}
----------------------------
Charles Casper Stockham: {ccs_performat} ({ccs_format})
Diana DeGette: {dd_performat} ({dd_format})
Raymon Anthony Doane: {rad_performat} ({rad_format})
----------------------------
Winner: {winner_candidate}""")