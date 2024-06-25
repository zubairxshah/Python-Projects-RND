import random, os, time
print("\033[32m", "GAME CHARACTER BUILDER", "\033[0m")
print()

def rollDice(side):
  result = random.randint(1,side)
  return result
  
def health_c1():
  health = ((rollDice(6) * rollDice(12))/2) + 10
  return health
def strength_c1():
  strength = ((rollDice(6) * rollDice(8))/2) + 12
  return strength


while True:
  name1 = input("Enter first character's name: ")
  type1 = input("Define your first character's type (Human, Elf, Dwarf, Orc): ")
  health1 = health_c1()
  strength1 = strength_c1()
  print()
  print(name1)
  print("HEALTH: ", health1)
  print("STRENGTH: ", strength1)
  print()
  print("Now create your second character.")
  name2 = input("Enter second character's name: ")
  type2 = input("Define your second character's type (Human, Elf, Dwarf, Orc): ")
  health2 = health_c1()
  strength2 = strength_c1()
  print()
  print(name2)
  print("HEALTH: ", health2)
  print("STRENGTH: ", strength2)
  
  #again = input("Do you want to create another character? ")
  #if again == "no" or again == "no" or again == "n":
  print()
  break
time.sleep(1)
os.system("clear")
round = 1
winner = None
print()
print("⚔️ BATTLE TIME ⚔️")
while True:
  diceC1 = rollDice(6)
  diceC2 = rollDice(6)
  print()
  if round == 1:
    print("Round", round, "The battle begins!")
    print()
  else:
    print("Round", round, "The battle continues!")
    print()
  
  if diceC1 > diceC2:
    print(name1, "wins the round ", round, ".")
    damage = abs(strength1 - strength2) + 1
    health2 -= damage
    print(name2, "takes a hit, with", damage, "damage!")
    print()
    print(name1)
    print("HEALTH: ", health1)
    print()
    print(name2)
    print("HEALTH: ", health2)
  elif diceC2 > diceC1:
    print(name2, "wins the round ", round, ".")
    damage = abs(strength2 - strength1) + 1
    health1 -= damage
    print(name1, "takes a hit, with", damage, "damage!")
    print()
    print(name1)
    print("HEALTH: ", health1)
    print()
    print(name2)
    print("HEALTH: ", health2)
  else:
    print("There shields 🛡 intercept the damage, No damage taken!")
  if health1 <= 0:
    winner = name2
    print()
    print("\033[31m",name1, "has died!","\033[0m")
    print("\033[32m", name2,"wins the battle! 🏹","\033[0m")
    break
  elif health2 <= 0:
    winner = name1
    print()
    print("\033[31m",name2, "has died!","\033[0m")
    print("\033[32m", name1,"wins the battle! 🏹","\033[0m")
    break
  else:
    round += 1
    continue

time.sleep(5)
os.system("clear")
print("⚔️ RESULT TIME ⚔️")
print()
print(winner, "has won in", round, "rounds.")