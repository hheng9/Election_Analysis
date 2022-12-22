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

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:

        # print(election_data)
        # # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        # # Print each row in the CSV file.
        # for row in file_reader:
        #     print(row)
        # Print the header row.
        headers = next(file_reader)
        print(headers)


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






