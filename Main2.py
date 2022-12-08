import random
class Game:
  def __init__(self,enemyHp,level,gold,playerHp,block):
    self.enemyHp=enemyHp
    self.level=level
    self.gold=gold
    self.playerHp=playerHp
    self.block=block
    self.currentHp=self.playerHp
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
    inventory=["attack","defend","attack","defend","attack","defend"]
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
      turn(attack["damage"],0)
    if(move == "smite"):
      turn(smite["damage"],0)
    if(move == "defend"):
      turn(0,defend["block"])
    
      
def turn(damage,block):
  global game
  game.block+=block
  hit=5
  game.block-=hit
  if((game.currentHp+game.block)<=game.playerHp):
    game.currentHp+=game.block
  elif((game.currentHp+game.block)>game.playerHp):
    game.currentHp=game.playerHp
  print("Your remaining hp is:",game.currentHp)
  game.enemyHp -= damage
  game.block=0
  print("your remaining block is:",game.block)
  print("your opponent has:",game.enemyHp,"hp left")
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
