# phrase = "it's outta here!!"
# print(phrase.upper())

# print("==================================")
# player_name = "    BJ Upton"
# print(player_name.lstrip().replace("BJ", "Melvin"))
# print(len(player_name))
# print("==================================")
# team1_runs = 8
# team2_runs = 5
# total_runs = team1_runs + team2_runs
# print(total_runs == 13)



#this code is for ...

# team1_runs = 8 
# team2_runs = 6
# team1_won =team1_runs > team2_runs
# team2_won = team1_runs < team2_runs
# teams_tied = team1_runs == team2_runs
# teams_did_not_tie = team1_runs != team2_runs
# print(type(team1_won))
# print(teams_did_not_tie)
# if team1_won:
#     message = "Nice Job Team1!!!"
# elif team2_won:
#     message = "way to go team 2!".title()
# else:
#     message = "must have tied!".title()
# print(message)
# print("7th ining stretch!!!!!!!!!!!".upper())
# print("take me out to the baaallll game, take me out to the crowwwwd!".upper())



print("\n==================================")
roster_list = ['clayton kershaw' , 'mookie betts' , 'cody bellinger', 'freddy freeman']

roster_list_upper = ['' , '' , '', '']
i = 0
for player in roster_list:
    roster_list_upper[i] = player.title()
    i = i + 1
print(roster_list_upper)
roster_dict = {
    'P': 'clayton kershaw',
    'RF': 'mookie betts',
    'CF': 'cody bellinger', 
    '1B': 'freddy freeman', 
}
roster_dict2 = {
    'P': {'name': 'clayton kershaw', 'throws': 'left', 'bats': 'left'},
    'RF': {'name': 'mookie betts', 'throws': 'right', 'bats': 'right'},
    'CF': {'name': 'cody bellinger', 'throws': 'right', 'bats': 'switch'}, 
    '1B': {'name': 'freddy freeman', 'throws': 'left', 'bats': 'left'}, 
}
bats = {
    'left': [],
    'right': [],
    'switch': []
}
for position in roster_dict2:
    player = roster_dict2[position]
    # print(f"player name: {player['name']}")
    # print(f"position: {position}")
    # print(f"player throws: {player.get('throws')}")
    # print(f"player bats: {player.get('bats')}")
    if (player['bats'] == 'left'):
        bats['left'].append(player['name'])
    elif (player['bats'] == 'right'):
        bats['right'].append(player['name'])
    elif (player['bats'] == 'switch'):
        bats['switch'].append(player['name'])
    
for handedness, players in bats.items():
    if handedness == 'left':
        print('The following players bat left-handed')
    elif handedness == 'right':
        print('The following players bat right-handed')
    elif handedness == 'switch':
        print('The following players bat switch')
    for player in players:
        print(player.title())



# for position, player in roster_dict.items():
#     print(f"position: {position}")
#     print(f"player: {player}")
    
