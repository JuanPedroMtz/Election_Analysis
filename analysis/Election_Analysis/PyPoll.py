# The data we need to retrieve
# 1. Total number of votes cast 
# 2. Complete list of candidates who received votes 
# 3. % of votes each candidate has 
# 4. Total of votes each candidate has 
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}
# WINNER!! 
winner_candidate = ""
winning_count = 0
winning_percentage = 0

# Counties
county_options = []
county_count = {}

# Biggest county 
biggest_county = ""
biggest_county_count = 0
biggest_county_percentage = 0



# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    # Read the headers row 
    headers = next(file_reader)
    
    # Get in each row
    for row in file_reader:

        # Count the candidates and counties
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

             # Start with candidates votes count 
            candidate_votes[candidate_name] = 0

        # If the county does not match any existing county...
        if county_name not in county_options:

            # Add it to the list of candidates.
            county_options.append(county_name)

             # Start with candidates votes count 
            county_count[county_name] = 0
            
            
        # Add to the total vote count.
        total_votes += 1

        # Adding votes
        candidate_votes[candidate_name] += 1
        county_count[county_name] += 1
    
    # Send results to text file
    with open(file_to_save, "w") as txt_file: 
        election_results = (f"Election Results\n---------------------------------\nTotal Votes: {total_votes}\n---------------------------------\n")
    
        print(election_results, end = "") 

        txt_file.write(election_results)
        


        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]

            vote_percentage = float(votes) / float(total_votes) * 100
        
            # Printing information about each candidate
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
        
            # Winner information
            if (votes > winning_count) and (vote_percentage > winning_percentage): 
                winning_count = votes 
                winner_candidate = candidate_name
                winning_percentage = vote_percentage
        
        # Winner candidate Sumamry
        winner_candidate_summary = (f"---------------------------------\nThe winner is {winner_candidate} with a total of {winning_count:,} votes and with the {winning_percentage:.1f}%\n---------------------------------\n")
        print(winner_candidate_summary)
        txt_file.write(winner_candidate_summary)

        for county_name in county_count:
            cvotes = county_count[county_name]

            cvote_percentage = float(cvotes) / float(total_votes) * 100
        
            # Printing information about each county
            county_results = (f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
            print(county_results)
            txt_file.write(county_results)
        
            # Biggest county
            if (cvotes > biggest_county_count) and (cvote_percentage > biggest_county_percentage): 
                biggest_county_count = cvotes 
                biggest_county = county_name
                biggest_county_percentage = cvote_percentage
            
        # Biggest county Sumamry
        biggest_county_summary = (f"---------------------------------\nThe county with the most turnout is {biggest_county} with a total of {biggest_county_count:,} votes and with the {biggest_county_percentage:.1f}%")
        print(biggest_county_summary)
        print("---------------------------------\n")
        txt_file.write(biggest_county_summary)
                







