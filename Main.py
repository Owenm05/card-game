import random
class Game:
  def __init__(self,enemyHp,level,gold):
    self.enemyHp=enemyHp
    self.level=level
    self.gold=gold
if __name__ == "__main__":
    game= Game(50,random.randint(1,3),100)
attack = {
  "damage": 5,
  "cost": 1,
  "flavor": "you swing your sword"
}
smite = {
    "damage":25,
    "cost":1,
    "flavor":"they all shall pay"
}
def shop(gold):
    global game
    print("welcome to my shop would you like to buy anything")
    global inventory
    inventory=["attack","defend"]
    cards=[]
    print("your level is :",game.level)
    if game.level>=1:
        cards=["attack","defend","heal"]
    if game.level>=2:
        cards.append("curse")
        cards.append("sacrifice")
    if game.level==3:
        cards.append("smite")
    answer = input()
    if answer == "yes":
      print("we have these cards:")
      for x in cards:
          print(x)
      print("what would you like to buy",cards)
      gear = input()
      if gear in cards:
          gear_id = cards.index(gear)
          if game.gold >= 10:
              print("you have purchased an", cards[gear_id], "card")
              game.gold -= 10
              print("you now have", + game.gold,"gold")
              inventory.append(gear)
              return game.gold
          elif game.gold<10:
              print("you dont have enough gold")
              print("you now have", + game.gold)
             
      else:
           print("no such card")
    if answer=="no":
      combat()
def combat():
    print("your cards include:")
    for x in inventory:
        print(x)
    hand=[]
    i=0
    while(i<=4):
      hand.append(inventory[random.randint(1,(len(inventory)-1))])
      i+=1
    print(hand)
    move=input("what card do you want to play?")
    if(move == "attack"):
      damage(attack["damage"])
      
def damage(damage):
  global game
  print(game.enemyHp)
  game.enemyHp -= damage
  print(game.enemyHp)
  combat()
shop(100)
restart=input("continue?")
import random
class Game:
  def __init__(self,enemyHp,level,gold):
    self.enemyHp=enemyHp
    self.level=level
    self.gold=gold
if __name__ == "__main__":
    game= Game(50,random.randint(1,3),100)
attack = {
  "damage": 5,
  "cost": 1,
  "flavor": "you swing your sword"
}
smite = {
    "damage":25,
    "cost":1,
    "flavor":"they all shall pay"
import random
class Game:
  def __init__(self,enemyHp,level,gold,playerHp,block):
    self.enemyHp=enemyHp
    self.level=level
    self.gold=gold
    self.playerHp=playerHp
    self.block=block
if __name__ == "__main__":
    game= Game(50,1,100,50,0)
attack = {
  "damage": 5,
  "cost": 1,
  "flavor": "you swing your sword"
}
smite = {
    "damage":25,
    "cost":1,
    "flavor":"they all shall pay"
}
defend = {
    "block":10,
    "cost":1,
    "flavor":"you raise your shield"
}
def shop(gold):
    global game
    print("welcome to my shop would you like to buy anything")
    global inventory
    inventory=["attack","defend"]
    cards=[]
    print("your level is :",game.level)
    if game.level>=1:
        cards=["attack","defend","heal"]
    if game.level>=2:
        cards.append("curse")
        cards.append("sacrifice")
    if game.level==3:
        cards.append("smite")
    answer = input()
    if answer == "yes":
      print("we have these cards:")
      for x in cards:
          print(x)
      print("what would you like to buy",cards)
      gear = input()
      if gear in cards:
          gear_id = cards.index(gear)
          if game.gold >= 10:
              print("you have purchased an", cards[gear_id], "card")
              game.gold -= 10
              print("you now have", + game.gold,"gold")
              inventory.append(gear)
              return game.gold
          elif game.gold<10:
              print("you dont have enough gold")
              print("you now have", + game.gold)
             
      else:
           print("no such card")
    if answer=="no":
      combat()
def combat():
    print("your cards include:")
    for x in inventory:
        print(x)
    hand=[]
    i=0
    if(len(inventory)>=5):
      while(i<=5):
        hand.append(inventory[random.randint(0,(len(inventory)-1))])
        i+=1
    if(len(inventory)<5):
      while(i<=len(inventory)):
        hand.append(inventory[random.randint(0,(len(inventory)-1))])
        i+=1
    print(hand)
    move=input("what card do you want to play?")
    if(move == "attack"):
      damage(attack["damage"])
    if(move == "smite"):
      damage(smite["damage"])
    
      
def damage(damage):
  global game
  print(game.enemyHp)
  game.enemyHp -= damage
  print(game.enemyHp)
  combat()
shop(100)
restart=input("continue?")
if restart=="yes":
    x=10
    gold=100-x
    x+=10
    shop(gold)
if restart=="no":
    combat()

