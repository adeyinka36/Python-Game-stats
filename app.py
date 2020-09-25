import constants 
import sys
import copy

def playGame():
    
    players=[]

    PLAYERS=copy.deepcopy(constants.PLAYERS)

    

    

    for p in PLAYERS :
        if p["experience"]=="YES":
            p["experience"]=True
        else:
            p["experience"]=False
        p["guardians"] = p["guardians"].split("and")
        height=p["height"].split(" ")
        p["height"]=int(p["height"][0]+p["height"][1])

        players.append(p)



    Panthers=[]
    Bandiths=[]
    Warriors=[]

    teams =[Panthers,Bandiths,Warriors]
    players_per_team= len(players)/len(teams)

    inexperienced=[]
    experienced=[]

    for p in players:
        if p["experience"] == True:
            experienced.append(p)
        else:
            inexperienced.append(p)

    # allocating players to teams
    for team in teams:
        while len(team)<players_per_team:
            team.append(inexperienced.pop())
            team.append(experienced.pop())


    print("Hello wecome to the game")
    print("Here are your choices")

    print("1) choose a team")
    print("2) quit ")

    choice = input("Please make a chioce: ")

    if int(choice) == 2:
        print("Bye")
        sys.exit()

    elif int(choice) == 1:
        print("1) Panthers")
        print("2) Bandiths ")
        print("3) Warriors ")

        team_choice = input("please choose a team by entering its number: ")

        team_choice = int(team_choice)-1

    print(f"Team Name: {constants.TEAMS[team_choice]}")
    print(f"Team size: {len(teams[team_choice])}")
    players_in_team=[]
    seperator=", "
    for player in teams[team_choice]:
        players_in_team.append(player["name"])

    print(f'Team Players:{seperator.join(players_in_team)}')

    experienced_count=0
    for p in teams[team_choice]:
        if p["experience"]:
            experienced_count+=1

    print(f"Number of experienced players: {experienced_count}")
    print(f"Number of inexperienced players: {6-experienced_count}")


    average_height =0

    for p in teams[team_choice]:
        average_height+=int(p["height"])

    average_height=average_height/len(teams[team_choice])

    print(f"Team average height:{average_height}")


    all_guardians=[]

    for p in teams[team_choice]:
        while len(p["guardians"]) > 0:
            all_guardians.append(p["guardians"].pop())

    all_guardians=", ".join(all_guardians)

    print(f"Guardians of  all the team playes are {all_guardians}")


    print("press Q to quite")

    back = input("Press any other  key to continue... ")

    if back == "q":
        print("Thanks for playing")
        sys.exit()

    else:
        return playGame()       


playGame()

    



