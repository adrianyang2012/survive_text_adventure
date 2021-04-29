
def game_over(message):
  print(message)
  yn = input("do you want to play again > ")
  if yn == "yes" or yn == "yep" or yn == "of course":
    start()
  else:
    with open("rates.txt","a") as rates:
      stars = input("how many stars")
      rates.write(input("how would you rate this game"))
      rates.write(f"{stars} stars")
    print("thanks for playing")
    exit("done")

def hot_tub():
  print("not very polite football players are chatting they start staring at you")
  print("you see a small exit very close")
  choice = input("> ")
  if "football" in choice:
    game_over("they bully you")
  elif "exit" in choice:
    game_over("you win! you went home! congragulations!")
def shop():
  print("you saw loots of mean buys")
  print("you brang a stick from the cave")
  print("you see a bathroom and a door and you see a emergency door")
  choice = input("> ")
  if "bathroom" in choice:
    print("done pooping")
    shop()
  elif "stick" in choice:
    game_over("they are to mean  and strong")
  elif "emergency" in choice:
    hot_tub()
  else:
    game_over("you go out the door but you broke the glass so you get cought by a police")
def cave():
  print("you see a bear")
  print("you see a path out")
  print("you see a chest inside the cave")
  print("there is a leading place to a city")
  choice = input("> ")
  if "chest" in choice:
    game_over("the bear wakes up and catches you for super")
  elif "out" in choice:
    game_over("you go out the cave and you arrive at a hot place")
  else:
    print("you went to a city! you got out and went a shop!")
    shop()
def jungle():
  print("you see a hill near you ")
  print("then a monkey swings and clears of a leaf and you see a cave")
  print("there is a parrot playing above")
  print("what do you do ?")
  choice = input("> ")
  if "hill" in choice:
    grassy_hills()
  elif "cave" in choice:
    cave()
  else:
    game_over("you catch the parrot and the tiger are mad")
def dessert():
  print("you see a very dry village on the left and a jungle peaking out of  a big tree")
  print("what do you do")
  choice = input("> ")
  if "village" in choice:
    game_over("you try to aks the villagers to give you water but they don't have water")
  elif "jungle" in choice:
    jungle()
def grassy_hills():
  print("you are in a very grassy hils you see a dessert, pond, jungle")
  print("what do you do ?")
  choice = input("> ")
  if "dessert" in choice:
    dessert()
  elif "pond" in choice:
    game_over("a crocadile snaps you up")
  else:
    jungle()
def start():
  name = input("what is you name")
  grassy_hills()
# ------------------main-----------------------------------#
start()
