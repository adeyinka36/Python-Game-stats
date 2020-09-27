import constants 
import sys
import copy
if  __name__== "__main__":
    def convert_to_int(str):
        try:
            num= int(str)
            return num
        except:
            return False
    
    def check_range(num,start,stop):
        res= range(start, stop)
        if num in res:
            return True
        else:
            return False
    
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
        print("Here are your choices:")
        print("\n")

        print("1) choose a team")
        print("2) quit ")
        print("\n")

        choice = input("Please make a chioce: ")
        print("\n")
        
        choice = convert_to_int(choice)
        if(choice):
            in_range = check_range(choice,1,3)
        
    
        while choice  == False or in_range == False:
            choice = input("Please make a choice from the opitions: ")
            choice = convert_to_int(choice)
            in_range = check_range(choice,1,3)

        

        
        if  choice == 2:
            print("Bye")
            sys.exit()

        elif choice == 1:
            print("1) Panthers")
            print("2) Bandiths ")
            print("3) Warriors ")
            print("\n")


        team_choice = input("please choose a team by entering its number: ")
        print("\n")


        team_choice = convert_to_int(team_choice)
        if(team_choice):
            in_range_team = check_range(team_choice,1,4)
        
        while team_choice  == False or in_range_team == False:
            team_choice = input("Please make a choice from the opitions: ")
            team_choice = convert_to_int(team_choice)
            in_range_team = check_range(team_choice,1,4)
        
        team_choice = team_choice-1

        

        print(f"Team Name: {constants.TEAMS[team_choice]}")
        print(f"Team size: {len(teams[team_choice])}")
        players_in_team=[]
        seperator=", "
        for player in teams[team_choice]:
            players_in_team.append(player["name"])

        print(f'Team Players: {seperator.join(players_in_team)}')

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
        print("\n")


        print("press Q to quit")

        back = input("Press any other  key to continue... ")

        if back.lower() == "q":
            print("Thanks for playing")
            sys.exit()

        else:
            return playGame()       

    
    playGame()

        



