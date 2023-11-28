import random, os, time

def rollDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = ((rollDice(6)*rollDice(12))/2)+10
  return healthStat

def strength():
  strengthStat = ((rollDice(6)*rollDice(8))/2)+12
  return strengthStat

print("⚔️ BATTLE TIME ⚔️")
print()
n1 = input("Name your Legend:\n")
t1 = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(n1)
h1 = health()
s1 = strength()
print("HEALTH:", h1)
print("STRENGTH:", s1)
print()
print("Who are they battling?")
print()

n2 = input("Name your Legend:\n")
t2 = input("Character Type (Human, Elf, Wizard, Orc):\n")
print()
print(n2)
h2 = health()
s2 = strength()
print("HEALTH:", h2)
print("STRENGTH:", s2)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print("The battle begins!")

  d1 = rollDice(6)
  d2 = rollDice(6)

  dif = abs(s1 - s2) + 1

  if d1 > d2:
    h2 -= dif
    if round==1:
      print(n1, "wins the first blow")
    else:
      print(n1, "wins round", round)
  elif d2 > d1:
    h1 -= dif
    if round==1:
      print(n2, "wins the first blow")
    else:
      print(n2, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)

  print()
  print(n1)
  print("HEALTH:", h1)
  print()
  print(n2)
  print("HEALTH:", h2)
  print()

  if h1<=0:
    print(n1, "has died!")
    winner = n2
    break
  elif h2<=0:
    print(n2, "has died!")
    winner = n1
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    
time.sleep(1)
os.system("clear")
print("⚔️ BATTLE TIME ⚔️")
print()
print(winner, "has won in", round, "rounds")
