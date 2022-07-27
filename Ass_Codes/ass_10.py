team_ind = {}
for i in range(11):
    player = input("Enter the Name of player:")
    height = float(input("Enter the height of player:"))
    team_ind[player] = height
print(team_ind)
captain = max(team_ind,key=team_ind.get)
print("Team India\nCaptain :",captain)