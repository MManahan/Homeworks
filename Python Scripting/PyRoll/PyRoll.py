import os
import csv

# Set path for CSV file

poll_csv_path = os.path.join("Resources", "election_data.csv")

# Open and Read CSV File
with open(poll_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)

    Votes = []
    Candidates = []

    # After printing out Candidates[], and knowing their indexes
    # I'm assigning these variables to their respective candidate index
    # to be used in the for loop 
    Khan_vote_counter = 0 
    Khan_percentage = 0    
    Correy_vote_counter = 0
    Correy_percentage = 0
    Li_vote_counter = 0 
    Li_percentage = 0
    Tooley_vote_counter = 0
    Tooley_percentage = 0

    for row in csv_reader:
        #count # votes
        Votes.append(row[0])

        #find each candidate and place them in list
        if row[2] not in Candidates:
            Candidates.append(row[2])
        
        # Because I know which index is candidate is assigned to, 
        # I am check each row in column2 to see if the name matches
        # If so, I am counting the # of votes for each candidate
        if row[2] == Candidates[0]:
            Khan_vote_counter = Khan_vote_counter + 1
        elif row[2] == Candidates[1]:
            Correy_vote_counter = Correy_vote_counter + 1
        elif row[2] == Candidates[2]:
            Li_vote_counter = Li_vote_counter + 1
        elif row[2] == Candidates[3]:
            Tooley_vote_counter = Tooley_vote_counter + 1

Total_Votes = len(Votes) # The # of Votes
# Finding percentages for each candidate
Khan_percentage = (Khan_vote_counter/Total_Votes)*100
Correy_percentage = (Correy_vote_counter/Total_Votes)*100
Li_percentage = (Li_vote_counter/Total_Votes)*100
Tooley_percentage = (Tooley_vote_counter/Total_Votes)*100


print('Election Results')
print('---------------------------')
print(f'Total Votes = {Total_Votes}')
print('---------------------------')
print(f'{Candidates[0]}: {round(Khan_percentage,2)}% ({Khan_vote_counter})')
print(f'{Candidates[1]}: {round(Correy_percentage,2)}% ({Correy_vote_counter})')
print(f'{Candidates[2]}: {round(Li_percentage,2)}% ({Li_vote_counter})')
print(f'{Candidates[3]}: {round(Tooley_percentage,2)}% ({Tooley_vote_counter})')
print('---------------------------')
print(f'Winner: {Candidates[0]}')
print('---------------------------')

output_results = open('PyPoll_output.txt', 'w')

output_results.write('Election Results\n')
output_results.write("--------------------------\n")
output_results.write(f'Total Votes = {Total_Votes}\n')
output_results.write('--------------------------\n')
output_results.write(f'{Candidates[0]}: {round(Khan_percentage,2)}% ({Khan_vote_counter})\n')
output_results.write(f'{Candidates[1]}: {round(Correy_percentage,2)}% ({Correy_vote_counter})\n')
output_results.write(f'{Candidates[2]}: {round(Li_percentage,2)}% ({Li_vote_counter})\n')
output_results.write(f'{Candidates[3]}: {round(Tooley_percentage,2)}% ({Tooley_vote_counter})\n')
output_results.write('---------------------------\n')
output_results.write(f'Winner: {Candidates[0]}\n')
output_results.write('---------------------------\n')


output_results.close()

        