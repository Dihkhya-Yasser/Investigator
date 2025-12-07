class Room:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
    
    def get_name(self):
        return self.__name
    
    def get_description(self):
        return self.__description
    
    def check_room(self):
        return f"{self.get_name()}: {self.get_description()}"

main_entrance = Room("Main Entrance", "The front 'door' is partially broken, with muddy 'footprints' and scattered blood stains at the 'threshold'")
living_room = Room("Living Room", "'Furniture' is in complete disarray: overturned couches, a table out of place, a prominent bloodstain on the carpet, broken cups and hurriedly stubbed cigarette butts, all signs of a fierce fight and skirmish")
kitchen = Room("Kitchen", "A large kitchen knife is missing from the 'rack', there are blood stains on the 'sink', bloody tissues in the 'trash', and the 'side door' has evidence of a recent break-in—suggesting forced entry")
main_bedroom = Room("Main Bedroom", "The 'bed' is in disarray with blood-stained sheets, there is the 'body' of a woman showing signs of resistance, beside her bed are opened 'drawers', an empty 'jewelry box', and torn 'paper' scattered around")
bathroom = Room("Bathroom", "There are diluted blood stains on the 'sink', a wet 'towel' thrown on the floor, an open 'bottle of cleaner', and a garment with fresh blood in the 'laundry basket'")

class Player:
    def __init__(self, name, position=None, evidence=None):
        self.__name = name
        if position == None:
            self.__position = main_entrance
        else:
            self.__position = position
        if evidence == None:
            self.__evidence = []
        else:
            self.__evidence = evidence
    
    def get_name(self):
        return self.__name
    
    def get_position(self):
        return self.__position
    
    def set_position(self, room):
        self.__position = room
    
    def get_evidence(self):
        return self.__evidence
    
    def add_evidence(self, item):
        self.__evidence.append(item)

name = input("What is your name? ")
player = Player(name)

print(f"Welcome {player.get_name()}. You are an assistant to an investigator. You received a message about a homicide in a house, and you have gone to the house with Investigator Charles and his team. You have just arrived. You must collect a lot of evidence while Charles investigates the neighbors and suspects.")
print("*How to play the game:")
print("Move: say 'go to' and press enter, then say the name of the place and press enter")
print("To observe and analyze the place: say 'check room'")
print("To document evidence: In the game, when you say 'check room', you will see a description. In the description, you will see words between single quotation marks (like 'blood'). You must say 'document', press enter, then say 'blood' and press enter.")
print("To check your evidence: say 'check evidence'")
print("To check the number of pieces of evidence: say 'check number of evidence'")
print("If you get enough evidence (12 items), say 'go to Charles'")

all_rooms = [main_entrance, living_room, kitchen, main_bedroom, bathroom]
all_rooms_names = ["Main Entrance", "Living Room", "Kitchen", "Main Bedroom", "Bathroom"]

print("")
print(f"The available rooms are: {all_rooms_names}")
print("The game has started. You are now at the Main Entrance of the house.")

all_evidence_items = ["door", "footprints", "threshold", "furniture", "rack", "sink", "trash", "side door", "bed", "body", "drawers", "jewelry box", "paper", "towel", "bottle of cleaner", "laundry basket"]
max_evidence = 16
min_win_evidence = 13

while True:
    opr = input("").lower()
    if opr == "check room":
        print(player.get_position().check_room())
    elif opr == "go to":
        while True:
            place = input("Enter room name: ").lower()
            found = False
            for room in all_rooms:
                if room.get_name().lower() == place:
                    player.set_position(room)
                    print(f"You are now in {room.get_name()}")
                    found = True
                    break
            if found:
                break
            else:
                print("Invalid input: check if the name of the room is correct")
                continue
    elif opr == "document":
        while True:
            write = input("Enter evidence name: ").lower()
            if write in all_evidence_items:
                if write in player.get_evidence():
                    print("Invalid input: you have already documented this.")
                    break
                else:
                    player.add_evidence(write)
                    print(f"You documented: {write}")
                    break
            else:
                print("Invalid input: that is not evidence.")
                break
    elif opr == "check evidence":
        print(player.get_evidence())
    elif opr == "check number of evidence":
        print(len(player.get_evidence()))
    elif opr == "go to charles":
        evidence_count = len(player.get_evidence())
        if evidence_count == max_evidence:
            work = "Good!"
            break
        elif evidence_count >= min_win_evidence:
            work = "OK"
            break
        else:
            print("You need more evidence.")
            continue
    else:
        print("Invalid input: this operation is not available")

print("")
print("You: Hmm, what a stupid killer. I haven't seen such a stupid killer in my life; he left a lot of evidence.")
print("You: Ok, I don't care. Anyway, I must take this evidence to Mr. Charles.")
print("You: Hey Mr. Charles!")
print("Charles: What is going on? Did you find any evidence?")
print("You: Heh... no... no, I didn't find a single piece of evidence.")
print("Charles: Hmm... I think the killer is planning very we... / You: Wait, let me finish. I mean I collected a lot of evidence, not just one piece.")
print(f"Charles: This is not the time for kidding, {player.get_name()}.")
print("You: Sorry sir, take the evidence.")

if work == "Good!":
    print(f"Charles: Hmm... the killer left a lot of evidence. I don't think his intention was to kill from the beginning. Anyway, excellent work {player.get_name()}, I will continue the investigation.")
else:
    print(f"Charles: Hmm... the killer left a lot of evidence. I don't think his intention was to kill from the beginning. Anyway, good work {player.get_name()}, I will continue the investigation.")
print("")
print("Thank you for playing my first game.")