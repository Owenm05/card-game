import random
def shop(gold):
    print("welcome to my shop would you like to buy anything")
    #gold = 100
    level=random.randint(1,3)
    inventory=[]
    cards=[]
    print("your level is :",level)
    if level>=1:
        cards=["attack","defend","heal"]
    if level>=2:
        cards.append("curse")
        cards.append("sacrifice")
    if level==3:
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
          if gold >= 10:
              print("you have purchased an", cards[gear_id], "card")
              gold -= 10
              print("you now have", + gold,"gold")
              inventory.append(gear)
              return gold
          elif gold<10:
              print("you dont have enough gold")
              print("you now have", + gold)
             
      else:
           print("no such card")
def combat():
    for x in inventory:
        print(x)
shop(100)
restart=input("continue?")
if restart=="yes":
    x=10
    gold=100-x
    x+=10
    shop(gold)
if restart=="no":
    combat()

