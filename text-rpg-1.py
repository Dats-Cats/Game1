# def battle0(enemy_money, enemy_hp):
#     global usr_money, usr_hp, running
#     print('Your HP: ', usr_hp, '. Enemy HP: ', enemy_hp)
#     while usr_hp>0 and enemy_hp>0:
#         time.sleep(0.1)
#         #user attack
#         damage = random.randint(0, 50)
#         print('you hit it with', damage)
#         enemy_hp-=damage
#         if enemy_hp<=0:
#             print('You won! HP left:',usr_hp)
#             money_gained=random.randint(1,enemy_money)
#             usr_money+=money_gained
#             print('Money added:',money_gained)
#             break
#         #enemy attack
#         damage=random.randint(0,30)
#         usr_hp-=damage
#         time.sleep(0.1)
#         print('it hit you with', damage)
#         if usr_hp <=0:
#             print('You failed!')
#             running=check_exit(9)
#     return usr_hp, running,



import random
import time

global running, user, rcount, inventory

running=True

rcount = 0
inventory=[]

class Сharacter:
    def __init__(self, hp, money, defence, weapon):
        self.hp= hp
        self.money = money
        self.defence=defence
        self.weapon=weapon
    def show_stats(self):
        print('HP:', self.hp)
        print('Money:', self.money)
        print('DMG:', self.dmg)
        print('DEF:', self.defence)


class item:
    def __init__(self, name, price):
        self.name=name
        self.price=price


class weapon(item):
    def __init__(self, name, price, dmg_min, dmg_max):
        super().__init__(name, price)
        self.dmg_min=dmg_min
        self.dmg_max=dmg_max

#---
def check_exit(usr_choose):
    if usr_choose==9:
        print('are you sure you want to exit?')
        print('1.yes')
        print('2.no')
        usr_choose = int(input('>'))
        if usr_choose==1:
            print('__________')
            print('GAME OVER')
            print('----------')
            print('Game finished with Exit code 0')
            return False
        elif usr_choose==2:
            print('Trying again')
            print()
            return True
    return True
#---
def HealingPotion(usr_choose):
    global inventory, user
    if 'Healing Potion' in inventory:
        if usr_choose == 5:
            print('You used Healing Potion')
            user.hp+=20
            user.hp=min(user.hp, 100)
            inventory.remove('Healing Potion')
    else:
        pass
    return user, inventory
#---
def minput():
    global inventory, usr_hp, running

    usr_choose = int(input('> '))
    HealingPotion(usr_choose)
    running = check_exit(usr_choose, rcount)
    return usr_choose
#---
def battle(enemy):
    global running, inventory, user
    print('Battle starts!')

    usr_def = 1
    # def_count=0
    # def_check=min(0,1)

    enemy_hp_save=enemy.hp

    while user.hp>0 and enemy.hp>0:
        time.sleep(0.2)
        print('')
     #   turn=random.randint(1,2)
        print('yourHP: ',user.hp)
        time.sleep(0.2)
        print()
        print('Your turn')
        print('What u gonna do?')
        time.sleep(0.2)
        print('1.Attack')
        time.sleep(0.2)
        print('2.Defend for 3 turns')
        time.sleep(0.2)
        print('3.Check enemy')
        time.sleep(0.2)



        # if def_check==1:
        #     def_count+=1
        # if def_count>=3:
        #     usr_def=1
        #     print()
        #     print('-Defend falls!')
        #     print()
        #     def_count=0
        #     def_check=0

        usr_choose = minput()

        #user step
        if usr_choose==1:

            damage = random.randint(user.weapon.dmg_min, user.weapon.dmg_max)
            enemy.hp -= damage
            print('You hit it with', damage, 'points')
            print('')

        elif usr_choose==2:
            usr_def=2
            print('damage decrased by 2 for 3 turns')
            print('')
            time.sleep(0.2)
            def_check=1

        elif usr_choose==3:
            print('Enemy HP:', enemy.hp)
            time.sleep(0.2)
            print('Enemy damage:',enemy.weapon.dmg_min, 'to', enemy.weapon.dmg_max)
            print('')
            time.sleep(0.2)


        #enemy step
        if enemy.hp >0:
            if enemy.hp<=20:
                if user.hp>20:
                    print('Enemy heals')
                    enemy.hp+=20
                    time.sleep(0.2)
                else:pass
            else:
                time.sleep(0.2)
                print('Enemy attacks!')
                damage=random.randint(enemy.weapon.dmg_min,enemy.weapon.dmg_max)
                user.hp-=damage//usr_def
                time.sleep(0.2)
                print('It hit you with ',damage,'points')
                time.sleep(0.2)


    if user.hp<=0:
        print('You failed!')
        running = check_exit(9, rcount)
    elif enemy.hp<=0:
        enemy.hp=enemy_hp_save
        print('You won!')
        m_gained=random.randint(0,enemy.money)
        print('Money added:', m_gained)
        user.money+=m_gained
        print('HP left:', user.hp)
#---
def shop():
    global user, inventory, running
    shoprunning=True
    print('You found a shop!')
    print('What to do?')
    print('1.Enter')
    print('2.Pass')

    usr_choose = minput()

    if usr_choose == 1:
        print('You entered the shop')
        print()
        while shoprunning:
            print('Money:', user.money)
            print('Inventory:', inventory)
            print('1.Healing potion - 20p.')
            print('   Heals 20HP')
            print('2.A silver sword - 120p')
            item=IronSword
            print('   Increases damage to', item.dmg_min, '-', item.dmg_max)
            print('8.Exit')

            usr_choose = minput()

            if usr_choose==1:
                item=HealingPotionI
                buy(item, weapon)

            elif usr_choose==2:
                item=IronSword
                buy(item,weapon)
                user.weapon=item
            if usr_choose==8:
                print('See you later!')
                shoprunning=False

#--
def buy(item, weapon):
    global inventory,user
    print('Are you sure? ',item.name,' costs ', item.price)
    print('1.Yes')
    print('2.No')
    usr_choose = minput()

    if usr_choose == 1 and user.money >= item.price:
        print('You bought ', item.name)
        inventory.append(item.name)
        user.money -= item.price
        pass
    elif usr_choose == 1 and user.money < item.price:
        print('')
        print('Cant afford!')
        print('')
        pass
    elif usr_choose==2:
        pass

#--------------------------------------------------------#

#ITEMS and WEAPONS PRESETS -->
HealingPotionI=item('Healing Potion',20)
Stick=weapon('Stick', 0, 20, 30)
IronSword=weapon('Iron Sword', 70,40,60)

#USER SPECS -->

user=Сharacter(100,100,20, Stick)
user.hp=min(user.hp,100)

#ENEMY PRESETS -->
goblin1=Сharacter(100,20,10, Stick)
goblin1.hp=min(goblin1.hp,100)


#--------------------------------------------------------#

#def base():
#global running, user, rcount, inventory
while running:
    print(running)
    if rcount == 0:
        print('____________')
        print('GAME STARTS')
        print('------------')
        user = Сharacter(100, 100, 20, Stick)
        user.hp = min(user.hp, 100)
    else:
        print('___________________')
        print('recursion happened')
    print("Money: ", user.money)
    print('Inventory:', inventory)
    print(user.weapon.name,'damage:', user.weapon.dmg_min, user.weapon.dmg_max)
    print('HP:', user.hp)
    print("Recursion count:", rcount)
    print('press 9 to exit')
    if 'Healing Potion' in inventory:
        print('press 5 to use Healing potion')
    print('choose a way')
    print('1.right')
    print('2.left')
    rcount +=1

    usr_choose = minput()


    if usr_choose==1:
        num_events = 1
        event=random.randint(1,num_events)
        if event==1:
            print('Goblin appear!')
            print('What to do?')
            print('1.Fight')

            usr_choose = minput()

            if usr_choose==1:
                enemy = goblin1
                battle(enemy)
                usr_choose = None
                continue

    if usr_choose==2:
        num_events = 1
        event = random.randint(1, num_events)
        if event == 1:

            shop()
            print("Ye")

            continue
