# OUTLINE OF THE PROJECT

# For the quarter finals in Champions League 8 teams are seeded.
# Assume the teams to be matched are following:
  # Roma, Barcelona, Juventus, Bayern Munich, Sevilla, Real Madrid, Manchester City, Liverpool

# The aim of the project is printing all possible combinations for the quarter final matches.
  # Note that Team1 v Team2 is equivalent to Team2 v Team1

# SOLUTION OF THE PROBLEM

teams = ["Roma", "Barcelona", "Juventus", "Bayern Munich", "Sevilla", "Real Madrid", "Manchester City", "Liverpool"]

i = 0
for team1 in teams:
  j = i+1
  while j < 8:
    team2 = teams[j]
    print (team1, "-", team2)
    j +=1
  i +=1
