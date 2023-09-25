# Imports
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip Header
    next(csvreader) 

    vote_count = 0
    chuck_count = 0
    diana_count = 0
    ray_count = 0
    chuck_per = 0
    diana_per = 0
    ray_per = 0
    winner = 0


    for row in csvreader:
        vote_count += 1
        if row[2] == "Charles Casper Stockham":
            chuck_count += 1
        if row[2] == "Diana DeGette":
            diana_count += 1
        if row[2] == "Raymon Anthony Doane":
            ray_count += 1

    chuck_per = round(((chuck_count / vote_count) * 100), 3)
    diana_per = round(((diana_count / vote_count) * 100), 3)
    ray_per = round(((ray_count / vote_count) * 100), 3)

    if ray_count > (chuck_count) and (diana_count):
        winner = "Raymon Anthony Doane"
    elif chuck_count > (diana_count) and (ray_count):
        winner = "Charles Casper Stockham"
    elif diana_count > (chuck_count) and (ray_count):
        winner = "Diana DeGette"

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {vote_count}")
    print(f"Charles Casper Stockham: {chuck_per}% ({chuck_count})")
    print(f"Diana DeGette: {diana_per}% ({diana_count})")
    print(f"Raymon Anthony Doane: {ray_per}% ({ray_count})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Export text
textpath = os.path.join("analysis", "analysistext")
with open (textpath, 'a') as out:
    out.write("Election Results")
    out.write("\n-------------------------")
    out.write(f"\nTotal Votes: {vote_count}")
    out.write(f"\nCharles Casper Stockham: {chuck_per}% ({chuck_count})")
    out.write(f"\nDiana DeGette: {diana_per}% ({diana_count})")
    out.write(f"\nRaymon Anthony Doane: {ray_per}% ({ray_count})")
    out.write("\n-------------------------")
    out.write(f"\nWinner: {winner}")
    out.write("\n-------------------------")
