print("Basic Algorithm for Xbow 3.0")
Cards={1:'Xbow',2:'Archers',3:'Knight',4:'Ice Spirit',5:'Skeletons',6:'Tesla',7:'Fireball',8:'Log'}
Deck=input("Are you facing Logbait?")
Cycle=input("What is your card cycle?")
print("If your cycle is", Cycle)
if Cards[1] in Cycle:
    if Cards[2] in Cycle:
        print("Split archers on the back and set up for Xbow at the bridge.")
    elif Cards[2] not in Cycle:
        print("Place Xbow at the bridge and enjoy the bloodshed.")
elif Cards[1] not in Cycle:
    if Cards[2] in Cycle:
        if Cards[4] in Cycle:
            print("Cycle ice spirit at the bridge.")
        elif Cards[4] not in Cycle:
            if Cards[5] in Cycle:
                if Deck=='Yes':
                    print("Cycle skeletons at the middle of your side of the arena.")
                elif Deck=='No':
                    print("Cycle skeletons in the back.")
            elif Cards[5] not in Cycle:
                if Deck=='Yes':
                    print("Cycle archers at the middle of your side of the arena.")
                elif Deck=='No':
                    print("Cycle log at the bridge.")
    elif Cards[2] not in Cycle:
        if Cards[4] in Cycle:
            print("Cycle ice spirit at the bridge.")
        elif Cards[4] not in Cycle:
           if Deck=='Yes':
               print("Cycle skeletons at the middle of your side of the arena.")
           elif Deck=='No':
               print("Cycle skeletons in the back.")