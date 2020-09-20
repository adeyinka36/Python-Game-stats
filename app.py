import constants 

players=[]

for p in constants.PLAYERS:
    if p["experience"]=="YES":
        p["experience"]=True
    else:
        p["experience"]=False
    height=p["height"].split(" ")
    p["height"]=int(p["height"][0]+p["height"][1])

    players.append(p)

print(players)
