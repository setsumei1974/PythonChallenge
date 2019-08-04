import os
import csv

csvpath = os.path.join("..", "ElectionData.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    TotalVotes = 0
    ListofCandidates = []
    
    VotesforKhan = 0
    VotesforCorrey = 0
    VotesforLi = 0
    VotesforOTooley = 0
        
#Use a loop to calculate the total number of votes, and to add names to a list of candidates
    for row in csvreader:
        TotalVotes += 1
        ListofCandidates.append(row[2])

 #Use conditionals with counters to calculate the votes for individual candidates
        if (row[2] == "Khan"):
            VotesforKhan += 1
        elif (row[2] == "Correy"):
            VotesforCorrey += 1
        elif (row[2] == "Li"):
            VotesforLi += 1
        elif (row[2] == "O'Tooley"):
            VotesforOTooley += 1
    
#Use a variable to divide the votes for candidates by the total votes
    PercentKhan = VotesforKhan / TotalVotes
    PercentCorrey = VotesforCorrey / TotalVotes
    PercentLi = VotesforLi / TotalVotes
    PercentOTooley = VotesforOTooley / TotalVotes

 #Use a max function to determine the greatest number of votes as preparation for determination of the winner
    Winner = max(VotesforKhan, VotesforCorrey, VotesforLi, VotesforOTooley)

 #Use conditionals to convert the number of votes to the name of a candidate
    if Winner == VotesforKhan:
        UltimateWinner = "Khan"
    elif Winner == VotesforCorrey:
        UltimateWinner = "Correy"
    elif Winner == VotesforLi:
        UltimateWinner = "Li"
    elif Winner == VotesforOTooley:
        UltimateWinner = "O'Tooley"

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {TotalVotes}")
print(f"-------------------------")
print(f"Khan: {PercentKhan:.3%}({VotesforKhan})")    
print(f"Correy: {PercentCorrey:.3%}({VotesforCorrey})")
print(f"Li: {PercentLi:.3%}({VotesforLi})")
print(f"O'Tooley: {PercentOTooley:.3%}({VotesforOTooley})")
print(f"-------------------------")
print(f"Winner: {UltimateWinner}")
print(f"-------------------------")

output_file = os.path.join("..", "ElectionDataRevised.csv")

with open(output_file, "w",) as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {TotalVotes}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Khan: {PercentKhan:.3%}({VotesforKhan})\n")
    txtfile.write(f"Correy: {PercentCorrey:.3%}({VotesforCorrey})\n")
    txtfile.write(f"Li: {PercentLi:.3%}({VotesforLi})\n")
    txtfile.write(f"O'Tooley: {PercentOTooley:.3%}({VotesforOTooley})\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {UltimateWinner}\n")
    txtfile.write(f"-------------------------\n")