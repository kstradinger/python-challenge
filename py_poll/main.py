#Sweet, Sweet imports
import os
import csv

#path to CSV data
csv_path = os.path.join('..','python-challenge','election_data.csv')
#Identify and read CSV data
with open(csv_path, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
# Read header row
    csv_header= next(csv_reader)
    print(f'Header: {csv_header}')

    #Define variables
    total_votes=0
    candidate_list = []
    unique_candidate_list = []
    maximum_votes = 0
    #begin for loop
    for row in csv_reader:
        #Define columns as list variables
        voter_id = row[0]
        county = row[1]
        candidate = str(row[2])
        #count total # of voters
        total_votes = total_votes + 1
        #Identify candidates with votes 
        candidate_list.append(row[2])

   #make a list of unique candidate names for 
    for x in candidate_list:
            if x not in unique_candidate_list:
                unique_candidate_list.append(x)   
    #calculate vote count and percent for each candidate
    kahn_votes = candidate_list.count("Khan")
    kahn_pct= round((kahn_votes / total_votes)*100,2)
    print(f'Khan: {kahn_votes} Votes ({kahn_pct}%)')
        
    correy_votes = candidate_list.count("Correy")
    correy_pct=round((correy_votes/total_votes)*100,2)
    print(f'Correy:{correy_votes} Votes ({correy_pct}%)')
    
    li_votes = candidate_list.count("Li")
    li_pct=round((li_votes/total_votes)*100,2)
    print(f'Li:{li_votes} Votes ({li_pct}%)')
    
    otooley_votes = candidate_list.count("O'Tooley")
    otooley_pct = round((otooley_votes/total_votes)*100,2)
    print(f"O'Tooley:{otooley_votes} Votes ({otooley_pct}%)")
#Create a list of the vote ct for each candidate to make a winner variable
vote_list= [kahn_votes, correy_votes,li_votes,otooley_votes]
winner_vote_count = max(vote_list)
if winner_vote_count == kahn_votes:
    winning_candidate = "Kahn"
elif winner_vote_count == correy_votes:
    winning_candidate = "Correy"
elif winner_vote_count == li_votes:
    winning_candidate = "Li"
else :
    winning_candidate = "O'Tooley"
print(f'The winner of the election, with {winner_vote_count} votes is: {winning_candidate}')

#Print text file with results
with open("poll_results.txt","w+") as text_file:
    text_file.write('Election Results')
    text_file.write('----------------')
    text_file.write(f'Khan: {kahn_votes} Votes ({kahn_pct}%)')
    text_file.write(f'Correy:{correy_votes} Votes ({correy_pct}%)')
    text_file.write(f'Li:{li_votes} Votes ({li_pct}%)')
    text_file.write(f"O'Tooley:{otooley_votes} Votes ({otooley_pct}%)")
    text_file.write(f'The winner of the election, with {winner_vote_count} votes is: {winning_candidate}')