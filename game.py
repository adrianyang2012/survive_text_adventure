#by Adrian 
#completed version 0.0.2 on 4/29/2021
import time
things = {
    "author":"Adrian",
    "date_made":"5/3/2021",
    "current_date":time.strftime( "%D  %H %I %P",time.localtime()),
    "current":"0.0.2",

    "helpers":{"bug_cleaner":"Lucas","Date adder":"Lucas",
    "code tester":"sisters"
      }
}
rate_ = True
name = input("what is you name")
if name == things["author"] or name == things["helpers"]["bug_cleaner"]:
  print("--------------------editing mode-------------------------")
  rate_ = False
def game_over(message):
  print(message)
  yn = input("do you want to play again > ")
  if yn == "yes" or yn == "yep" or yn == "of course":
    start()
  else:
    if rate_:
      with open("rates.txt","a") as rates:
        rates.write(f"{name}:")
        stars = input("how many stars")
        rates.write(input("how would you rate this game")+":")
        rates.write(f"{stars}stars"+" ")
      print("thanks for playing")
      print("----------------credits-------------------")
      for i in range(0,30):
        print(" ")
      for x in things.keys():
        print(x,":",things[x])
      for i in range(0,20):
        print(" ")
      for i in range(0,30):
        time.sleep(0.08)
        print(" ")
    exit(keep_kernel=True)

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
  #fun stuff
  elif "piano" in choice:
    raise IndexError("there is no piano in the shop")
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

  print("lets go!")
  print("you been traped in a moutian and had to live in a forest for 3 weeks")
  grassy_hills()
# ------------------main-----------------------------------#
start()
