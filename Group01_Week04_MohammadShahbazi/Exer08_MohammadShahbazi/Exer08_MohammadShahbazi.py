votes = ["Candidate A", "Candidate B", "Candidate A", "Candidate C", 
         "Candidate B"]

votes_counts = {}

for vote in votes:
    if vote in votes_counts:
        votes_counts[vote] += 1
    else:
        votes_counts[vote] = 1
print("winner is :")
max_vote = 0
winner = ""
for candidate, count in votes_counts.items():
    if count > max_vote:
        max_vote = count
        winner = candidate
print(f"{winner} with {max_vote} votes")