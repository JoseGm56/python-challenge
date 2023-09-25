# Imports
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip Headers
    next(csvreader) 

    # Define some variables 
    month_counter = 0
    net_profit = 0
    increase = 0
    decrease = 0
    checker = 0
 
    # Find all of the months, net profit, starting value and ending value
    for row in csvreader:
        if month_counter == 0:
            start = row[1]
        month_counter += 1
        net_profit = net_profit + int(row[1])
        end = row[1]

        # Set the checker and the date
        checker = int(row[1]) - checker
        date = row[0]

        # Find biggest increase and its date
        if checker > increase:
            increase = checker
            date_inc = date

        # Find smallest increase and its date
        if checker < decrease:
            decrease = checker
            date_dec = date

        # Update the checker
        checker = int(row[1])

    # Calculate the average change
    change = (int(end) - int(start)) / (month_counter - 1)
    change = round(change, 2)

    # Print statements
    print("Finacial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${change}")
    print(f"Greatest Increase in Profits: {date_inc} (${increase})")
    print(f"Greatest Decrease in Profits: {date_dec} (${decrease})")
    
# Export Text file
textpath = os.path.join("analysis", "analysistext")
with open (textpath, 'a') as out:
    out.write("Finacial Analysis")
    out.write("\n----------------------------")
    out.write(f"\nTotal Months: {month_counter}")
    out.write(f"\nTotal: ${net_profit}")
    out.write(f"\nAverage Change: ${change}")
    out.write(f"\nGreatest Increase in Profits: {date_inc} (${increase})")
    out.write(f"\nGreatest Decrease in Profits: {date_dec} (${decrease})")