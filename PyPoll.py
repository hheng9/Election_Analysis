# Import the datetime class from the datetime module
import datetime as dt
# Use the now() attribute on the datetime class to get the present time 
now = dt.datetime.now()
# Print the present time
print("The time is right now", now)

import csv
dir(csv)

# # Assign a variable for a file to load an the path 
# file_to_load = 'Resources/election_results.csv'

# # Open the election results and read the file
# # election_data = open(file_to_load, 'r')
# with open(file_to_load) as election_data:

# # To do: perform analysis

# # Close the file.
# # election_data.close()
#     print(election_data)


# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")

# Create a filename to a direct or indeirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w"=write we will write data to the file.

# Initialize a total vote counter
total_votes = 0 

# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:

        # print(election_data)
        # # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        # # Print each row in the CSV file.
        # Print the header row.
        headers = next(file_reader)
        # print(headers)
        # # Print each row in the CSV file.
        for row in file_reader:
            # # 2. Add to the total vote count --- number = number + 1
            total_votes +=1
            # print(row)
# # 3. Print the total votes.
# print(total_votes)
            # Print the candidate name from each row.
            candidate_name = row[2]
            # If the candidate does not match any existing candidate....
            if candidate_name not in candidate_options:
                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)
                # 2. Begin tracking that candidate's votes count.
                candidate_votes[candidate_name]=0
            # Add a vote to that candidate's count.
            candidate_votes[candidate_name]+=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file: 
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # #Print the candidate list.
    # print(candidate_votes)

    # Determine the percentage of votes for each candidate by loopimg through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of candidate.
        votes=candidate_votes[candidate_name]
        # 3. Calculate the percentage of cotes.
        vote_percentage=float(votes)/float(total_votes)*100. 
        # # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}:received{vote_percentage:.1f}% of the vote.")
        
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    # print(f"{candidate_name}:{vote_percentage:.1f}%({votes:,})\n")

    # Determine the winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # To do: print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)


# # Create a filename to a direct or indeirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w"=write we will write data to the file.

# open(file_to_save, "w")


# # Create a file name variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file 
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# file_to_save = os.path.join("analysis", "election_analysis.txt")

# with open(file_to_save, "w") as txt_file:
#     # txt_file.write("hello World")
#     txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")