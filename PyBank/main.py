#!/usr/bin/env python
# coding: utf-8

# Import operating system and CSV packages
import os
import csv

# Declare files paths to CSV and Text files
csvpath = "Resources/budget_data.csv"
textpath = "Analysis/analysis.txt"

# Open CSV file as read-only with UTF-8 encoding
with open(csvpath, "r", encoding='utf8') as csvfile:
    # Read contents of CSV file into variable
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Bypass header row
    header = next(csvreader)
    
    # Initiate empty lists and declare initial value for "net"
    month = []
    pl = []
    plint = []
    change = []
    net = 0
    
    # Loop through rows
    for r in csvreader:
        # Append values for each month to "month" list
        month.append(r[0])
        
        # Append values for each month to "pl" list
        pl.append(r[1])
        
        # Calculate total of all values in "pl" list
        net = net + int(r[1])
        
        # Put profit & loss values into "plint" list as integers
        plint = [eval(i) for i in pl]
        
        # Calculate and add difference values to "change" list
        change = [y - x for x, y in zip(plint, plint[1:])]

# Calculate number of months
months = len(month)

# Format integer to U.S. currency
netcur = "${:,.2f}".format(net)

# Calculate average change
average = sum(change) / (months - 1)

# Format integer to U.S. currency
avgcur = "${:,.2f}".format(average)

# Assign maximum change value to variable
increase = max(change)

# Assign index position of maximum change value to variable
maxindex = change.index(increase)

# Assign month value of maximum change to variable
monmax = month[maxindex + 1]

# Format integer to U.S. currency
maxcur = "${:,.2f}".format(increase)

# Assign minimum change value to variable
decrease = min(change)

# Assign index position of minimum change value to variable
minindex = change.index(decrease)

# Assign month value of minimum change to variable
monmin = month[minindex + 1]

# Format integer to U.S. currency
mincur = "${:,.2f}".format(decrease)

# Print values to terminal
print(f"""Financial Analysis
----------------------------
Total Months: {months}
Total: {netcur}
Average Change: {avgcur}
Greatest Increase in Profits: {monmax} {maxcur}
Greatest Decrease in Profits: {monmin} {mincur}""")

# Open and write values to text file
with open(textpath, 'w') as text:
    text.write(f"""Financial Analysis
----------------------------
Total Months: {months}
Total: {netcur}
Average Change: {avgcur}
Greatest Increase in Profits: {monmax} {maxcur}
Greatest Decrease in Profits: {monmin} {mincur}""")