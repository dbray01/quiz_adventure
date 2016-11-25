# An adventure game
from random import randint

hp = 20
at = 0
de = 0

def startingroom():
    global hp, at, de
    

    print("You see a chest across the room and you decide to open it")
    chest = randint(1, 2)

    if chest == 1:
        print("You are blessed with Callums' pies")

    elif chest == 2:
        print("You do not gain Callums' pies. Instead you are rewarded with some sick clogs")

    print("As you advance beyond the chest, you can see two doors.")
    print("Which door do you wish to pass through?")
    print(" ")
    print("Left")
    print("Right")

    answer = input("Answer: ")

    if answer.upper()[0] ==  "L":
        print("In the room you see two goblins. However you cannot fight them as you do not own any weapons. Your only chioce is to go through the other door")
         
    elif answer.upper()[0] == "R":
        print("In this room there is a thin wooden beam set across a pool of lava where the floor has broke through")

    fall = randint(1, 10)

    if fall == 6:
         print("You fall rapidly to the lava and then you notice that the lava is fake. It bounces you up and slowly breaks your fall.")

    else:
        print("You make it to the other side safely and take a ladder going down. If you look beind you, you notice that the lava was fake and was actually a crash mat.")
        print(" ")
        room1()


def room1():
    global hp, at, de
   
    goblin_hp = 4
    goblin_dam=randint(1,2)

    print("After walking for a while you come across a snail")
    print("The snail speaks in a wise croaky voice 'You are in danger, i shall give you this old rusted sword and then you must advance in your journey.'")
    print(" ")
    print(" ") 
    attack = 2

    print("You sprint to find an exit to the dungeon and eventually you see light")
    print("After a while you realise it was another room in the dungeon and are ambushed by goblins")

    while hp > 0 and goblin_hp > 0:

        print("You take your stance and swing for the disgusting beast")
        goblin_hp = goblin_hp - attack

        print("The goblins jumps up and slashes its claws towards your face")
        hp = hp - goblin_dam

    if hp <= 0:
        print("You died")

    else:
        print("You slayed the mighty beast")
        print("Health:" ,hp)
        room2()

def room2():
    global hp, at, de

    print("You advance and you find 1 Health Potion")
    print("You can either drink it or leave")
    print("A. Drink the potion")
    print("B. Leave it")
    answer=input ("Answer: ")
    if answer.upper() == ("A"):
           hp=hp+3
    print("Health: ",hp)

    if answer.upper() == ("B"):
      print("You ignore the potion and advance")
    room3()
    
def room3():
    global hp, at, de
    
    print("As you keep walking the groud begins to shake and you sense there is an earthquake")
    print("You can do two things ")
    print("A. Sprint to avoid it")
    print("B. Act normal and hope that it isnt an earthquake")
    answer = input("Answer: ")
    if answer.upper()[0]==("B"):
       print("Your foolishness overpowers you. You are brutally destroyed by the unyeilding earthquake")
    if answer.upper()[0]==("A"):
        print("You run for a while. You are careless and you fall through the floor.")
        print("You take damage from your fall and you dont know where you are but it looks the exact same to every other room")
        hp = hp - 3
        print("Health: ",hp)
    print("You come across the wise snail again who gives you some armour.'You are doing well my wise one. Have some iron armour and an old sword'")
    de = de + 7
    at = at+ 10
    print("Defence: ",de)
    print("Attack: ",at)
    room4()

def room4():
    global hp, at, de

    print("You are now in a room with a large rat that seems extremely hostile")
    print("It starts to spit acid and dies")
    print("You sense there is a disease around this area however there is a very tempting bed. You havent slept in ages and have the choice to sleep or carry on")
    print(" ")
    print("A. Sleep to gain 5 health")
    print("B. Carry on")
    answer = input("Answer: ")
    if answer.upper()[0]==("A"):
      print("You sleep but you do not wake up. The disease that rat had carries on to you and you die. The End.")
    if answer.upper()[0]==("B"):
        print("You  advance in your journey and you step on a snail by accident.")
        print("A voice echoes throughout the dungeon. It sounds very familiar.")
        print("'How dare you! I shall meet you at the south-west tunnels. BE THERE!'")
        finalroom()

def finalroom():
       global hp, at, de

       snail_hp=38
       snail_at= randint (1, 8)


       print(" ")
       print(" ")
       print(" ")
       print("You have made it to the south-east tunnels and see a tiny silihoutee in the corner.")
       while hp > 0 and snail_hp > 0:
         print("The snail leaps on you and bites you. You take some damage")
         hp = hp - snail_at
         print("Health: ", hp)
         print("You fight back ant swing your sword.")
         snail_hp = snail_hp - at
       if snail_hp < 0:
         print("You win the mighty battle")
       if hp < 0:
         print("The snail defeats you. The End.")
        
           


    
    

     
    
        

          

   









# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    startingroom()
    
