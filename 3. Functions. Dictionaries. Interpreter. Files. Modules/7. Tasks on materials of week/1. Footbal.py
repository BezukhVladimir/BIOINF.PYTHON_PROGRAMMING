N = int(input())
teams = {}
firstTeam = ""
resultFirstTeam = 0
resultSecondTeam = 0
secondTeam = ""

for i in range(N):
    firstTeam, resultFirstTeam, secondTeam, resultSecondTeam = [int(i) if i.isdigit() else i for i in input().split(";")]
    if firstTeam not in teams:
        teams[firstTeam] = [0, 0, 0, 0, 0]
    if secondTeam not in teams:
        teams[secondTeam] = [0, 0, 0, 0, 0]
        
    teams[firstTeam][0]  += 1
    teams[secondTeam][0] += 1
    
    if resultFirstTeam > resultSecondTeam:
        teams[firstTeam][1]  += 1
        teams[firstTeam][4]  += 3
        teams[secondTeam][3] += 1
        
    elif resultFirstTeam < resultSecondTeam:
        teams[secondTeam][1] += 1
        teams[secondTeam][4] += 3
        teams[firstTeam][3]  += 1
        
    else:
        teams[firstTeam][2]  += 1
        teams[firstTeam][4]  += 1
        teams[secondTeam][2] += 1
        teams[secondTeam][4] += 1
        
for result in teams:
    print(result+':', *teams[result])