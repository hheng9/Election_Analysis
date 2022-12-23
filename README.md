# Election_Analysis

## Overview of Election Audit: Explain the purpose of this election audit analysis.

### The purpose of this election audit analysis is to calculate the votes by counties, candidates, turnover, totals, and percentages. The data collected from our Python script created in Visual Studio Code will help generate itemized information on the winning amount of total votes and filter the results as needed.

## Election Audit Results
* The election resulted in 369,711 total votes across all counties and all candidates.
* The number of votes and the percentage of total votes for each county in the precinct.
   * The county of Jefferson had 38,855 votes with 10.5% of the total votes.
   * The county of Denver had 306,055 votes with 82.8% of the total votes.
   * The county of Arapahoe had 24,801 votes with 6.7% of the total votes.
* The county of Denver came in with the largest amount of votes at 306,055 and 82.8% of the total votes.
* The number of votes and the percentage of the total votes each candidate received.
   * Charles Casper Stockham took in 85,213 votes averaging 23.0% of the total votes.
   * Diana DeGette took in 272,892 votes averaging 73.8% of the total votes.
   * Raymon Anthony Doane took in 11,606 votes averaging 3.1% of the total votes.
* Diana DeGette came in as election results winner.
   * Diana DeGette's vote count came in at 272,892
   * Diana DeGette's percentage was 73.8% of the total votes

## Election Results in Text Format 
![Election_Results_TXT](https://user-images.githubusercontent.com/118647523/209246846-cca13497-94f3-4fe8-a04d-921fa9dd3fb5.png)

## Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

### The election results were defined with necessary information to determine the winning election votes in counties and for candidates. The data stated the percentages based off of the total amount of the votes accumulated throughout the election. The PyPoll.py script can be edited or adjusted to performthe outcomes of other elections by editing the path of a new CSV sheet provided and editing the print function text to showcase the result findings of the new information.The script shown below can be altered or modified in other states for any counties or candidates if ever needed.

## Script Executed with Python in Visual Studio Code

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
#will hold county with most votes
Wcounty = ""
WcountyV = 0
WcountyP = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load, 'r') as election_data:
    file_reader = csv.reader(election_data)

    # Read the header
    header = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes +=1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
             county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
             county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        # county_votes[county_name] +=1
        county_votes[county_name] = county_votes[county_name] + 1
        # candidate_votes[candidate_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        Cvotes = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        CountyVP = float(Cvotes) / float(total_votes) *100

         # 6d: Print the county results to the terminal.
        county_results = (f'{county_name}: {CountyVP:.1f}% ({Cvotes:,})\n')
        print(county_results)   
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (Cvotes > WcountyV) and (CountyVP > WcountyP):
            WcountyV = Cvotes
            Wcounty = county_name
            WcountyP = CountyVP

    # 7: Print the county with the largest turnout to the terminal.
        winning_county_summary = (
        f"------------------------\n"
        f"County with highest turnout: {Wcounty}\n"
        f"Vote Count for {Wcounty}: {WcountyV:,}\n"
        f"Percentage of total votes for {Wcounty}: {WcountyP:.1f}%\n"
        f"------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

