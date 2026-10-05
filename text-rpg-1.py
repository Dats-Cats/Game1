
import random
import time
from ast import increment_lineno

global running, rcount,shoprunning, battle_running, user_lvl

user_lvl=1
running=True
rcount = 0
inventory=[]

class Character:
    def __init__(self,name, hp, money, weapon, armor):
        self.name=name
        self.hp= hp
        self.money = money
        self.weapon=weapon
        self.armor=armor
class item:
    def __init__(self, name, price, shop_text, sell_price, isItem):
        self.name=name
        self.price=price
        self.sell_price = sell_price
        self.shop_text=shop_text
        self.isItem=isItem
class weapon(item):
    def __init__(self, name, price, dmg_min, dmg_max, sell_price):
        super().__init__(name, price, shop_text=None, sell_price=sell_price, isItem=0)
        self.dmg_min=dmg_min
        self.dmg_max=dmg_max
class armor(item):
    def __init__(self, name, price, defence, sell_price):
        super().__init__(name, price, shop_text=None, isItem=0, sell_price=sell_price)
        self.defence=defence

#--
def chestevent(user):
    print('You found a chest hidden under leaves')
    item_list=['Coins', IronArmor,  IronSword, 'Mimic']
    drop=random.choice(item_list)
    print('Open it?')
    print('1.Yes')
    print('2.No')
    usr_choose=minput()
    if usr_choose==1:
        if drop=='Coins':
            m_gained=random.randint(10,50)
            print('You found tokens inside')
            print(m_gained,'points acquired')
            user.money+=m_gained
        if drop=='Mimic':
            print('The chest was mimic!')
            enemy=Mimic
            battle(enemy, user)
        else:
            if isinstance(drop, weapon):
                print('You found', drop.name)
                print('Want to equip it?')
                print('1.Yes')
                print('2.No')
                usr_choose = minput()
                if usr_choose == 1:
                    print('You equiped', drop.name)
                    user.weapon = drop
                elif usr_choose==2:
                    inventory.append(drop)
            elif isinstance(drop, armor):
                print('You found', drop.name)
                print('Want to equip it?')
                print('1.Yes')
                print('2.No')
                usr_choose=minput()
                if usr_choose==1:
                    print('You equiped',drop.name)
                    user.armor = drop
                elif usr_choose==2:
                    print(drop.name,'added to your inventory')
                    inventory.append(drop)
    elif usr_choose==2:
        print('You have passed by')
        pass
#---
def inv_print(inventory):
    lines=[]
    print()
    print('Inventory:')
    if len(inventory)==0:
        print('Nothing in stored')
        return None
    for num, item in enumerate(inventory, start=1):
        lines.append(f'{num}.{item.name}')
    return '\n'.join(lines)
#---
def equip(user, inventory, usr_choose):
    if usr_choose==9:
        print('Equipped items:')
        print('Armor: ', user.armor.name)
        print('Weapon:',user.weapon.name)
        print()
        print(inv_print(inventory))
        print('9. Exit')
        old_armor=user.armor
        old_wpn=user.weapon

        print('Insert item number to equip it')

        usr_choose=int(input('>'))
        if usr_choose>=1 and usr_choose<=len(inventory):
            item=inventory[usr_choose-1]
            if item.isItem==1:
                print('cant equip',item.name)
            elif isinstance(item, weapon):
                user.weapon=item
                inventory.remove(item)
                inventory.append(old_wpn)
                print(item.name, 'equipped')
                print(old_wpn.name , 'was returned to your inventory')
            elif isinstance(item, armor):
                user.armor=item
                inventory.remove(item)
                inventory.append(old_armor)
                print(item.name, 'equipped')
                print(old_armor.name ,'was returned to your inventory')
#---
def sell(inventory,user):
    print('Select item you want to sell')
    print(inv_print(inventory))
    print('Sell item')
    usr_choose = minput()
    if usr_choose >= 1 and usr_choose <= len(inventory):
        item = inventory[usr_choose - 1]
        print(f'Sell item {item.name} for {item.sell_price}?\n1.Yes\n2.No')
        usr_choose=minput()
        if usr_choose==1:
            print(item.name,'sold for',item.sell_price)
            user.money+=item.sell_price
            inventory.remove(item)
#---
def check_exit(usr_choose):
    global running, shoprunning, battle_running
    if usr_choose!=0:
        return True
    if usr_choose==0:
        print('are you sure you want to exit?')
        print('1.yes')
        print('2.no')
        while True:
            try:
                usr_choose = int(input('>'))
                break
            except ValueError:
                print('Only numbers included! Try again')
        if usr_choose==1:
            print('__________')
            print('GAME OVER')
            print('----------')
            print('Steps you did:', steps_list)
            print('Game finished with Exit code 0')
            shoprunning=False
            battle_running=False
            return False
        elif usr_choose==2:
            print('Trying again')
            print()
            return True

    return True
#---
def HealingPotion(usr_choose, user, inventory):
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
    global running
    while True:
        try:
            usr_choose = int(input('> '))
            HealingPotion(usr_choose, user, inventory)
            running=check_exit(usr_choose)
            equip(user, inventory, usr_choose)
            return usr_choose
        except ValueError:
            print('Only numbers included. Try again')
            continue
# ---
def battle(enemy, user):
    global running, battle_running, user_lvl
    usr_def = 1
    enemy_hp_save=enemy.hp
    enemy_heal_count=0
    battle_running=True
    print(enemy.name, ' appear!')
    print('What to do?')
    print('1.Fight')
    print('2.Try escape')
    usr_choose = minput()

    while battle_running and running:
        if usr_choose == 1:
            print('Battle starts!')
            while user.hp>0 and enemy.hp>0:
                print()
                time.sleep(0.1)
                print('')
             #   turn=random.randint(1,2)
                print('yourHP: ',user.hp)
                time.sleep(0.1)
                print()
                print('Your turn')
                print('What u gonna do?')
                time.sleep(0.1)
                print('1.Attack')
                time.sleep(0.1)
                print('2.Defend for 3 turns')
                time.sleep(0.1)
                print('3.Check enemy')
                time.sleep(0.1)
                print('4.Try escape')

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

                elif usr_choose==4:
                    escape_try = random.randint(1, 2)
                    if escape_try == 1:
                        print('You failed running away!')
                        pass
                    elif escape_try == 2:
                        print('You escaped!')
                        return user

                #enemy step
                if enemy.hp >0:
                    if enemy.hp<=20:
                        if user.hp>20 and enemy_heal_count<=3:
                            print('Enemy heals')
                            enemy.hp+=20
                            enemy_heal_count+=1
                            time.sleep(0.2)
                        else:pass
                    else:
                        time.sleep(0.2)
                        print('Enemy attacks!')
                        damage=random.randint(enemy.weapon.dmg_min,enemy.weapon.dmg_max)
                        user.hp-=damage//(usr_def*user.armor.defence)
                        time.sleep(0.2)
                        print('It hit you with ',damage,'points')
                        time.sleep(0.2)

            if user.hp<=0:
                print('You failed!')
                running = check_exit(9)
            elif enemy.hp<=0:
                enemy.hp=enemy_hp_save
                print('You won!')
                m_gained=random.randint(0,enemy.money)
                print('Money added:', m_gained)
                user.money+=m_gained
                user_lvl += 1
                return user

        elif usr_choose==2:
            escape_try=random.randint(1,2)
            if escape_try==1:
                print('You failed running away!')
                usr_choose=1
                continue
            elif escape_try==2:
                print('You escaped!')
                return user
#---
def shop_show(item):
    global shop_num_count
    shop_num_count += 1
    print(shop_num_count,'.',item.name,'-',item.price,'p')
    if item.shop_text != None:
        print(item.shop_text)
    if isinstance(item, weapon):
        print('   Increases damage:',item.dmg_min,'-',item.dmg_max)
    if isinstance(item,armor):
        print('   Increases defence to X',item.defence)
#---
def shop(user):
    global running, shoprunning, shop_num_count, user_lvl
    #DONT ADD TO SHOPLIST MORE THAN 7 VALUES!!!!!!!!
    shop_list = [HealingPotionI, IronSword, IronArmor]
    shoprunning=True
    print('You found a shop!')
    print('What to do?')
    print('1.Enter')
    print('2.Pass')

    usr_choose = minput()

    if usr_choose == 1:
        print('You entered the shop')
        print()
        while shoprunning and running:
            shop_num_count=0

            print('Money:', user.money)
            for i, item in enumerate(shop_list, start=1):
                shop_show(item)
            print('8.Exit shop')
            print('10.Sell items')

            usr_choose = minput()

            if 1<=usr_choose<=len(shop_list):
                item=shop_list[usr_choose-1]
                buy(item)
            if usr_choose==8:
                print('See you later!')
                shoprunning=False
            if usr_choose==10:
                sell(inventory,user)
    return user
#--
def buy(item):
    global inventory,user
    print('Are you sure? ',item.name,' costs ', item.price)
    print('1.Yes')
    print('2.No')
    usr_choose = minput()

    if usr_choose == 1 and user.money >= item.price:
        print('You bought ', item.name)
        inventory.append(item)
        user.money -= item.price
        pass
    elif usr_choose == 1 and user.money < item.price:
        print('')
        print('Cant afford!')
        print('')
        pass
    elif usr_choose==2:
        pass
#---
def EnemyGen(enemy):
    global rcount, user_lvl
    difficulty = (user_lvl + 3) // 3
    enemy_race = 1*(user_lvl//2)
    #names

    if enemy_race<=1:
        name_list = ['Goblin', 'Skeleton', 'Slime']
    elif enemy_race>=2:
        name_list=['Orc','GigaGoblin','GigaSkeleton']
    #weapons
    if enemy_race<=1:
        wpn_list=[Stick, Cane]
    elif enemy_race>=2:
        wpn_list=[IronSword, Knife]
    #armors
    if enemy_race<=1:
        armor_list=[SlaveRobe, ]
    elif enemy_race>=2:
        armor_list=[IronArmor, ]

    hp_base=50+(difficulty*20)

    enemy.name=random.choice(name_list)
    hp_prerounded=random.randint(hp_base-10,hp_base+20)
    enemy.hp=(round(hp_prerounded, -1))
    enemy.money=random.randint(difficulty*20-10,difficulty*20+10)
    enemy.weapon=random.choice(wpn_list)
    enemy.armor=random.choice(armor_list)

    return enemy
#--
def Start_storytell():
    print('Long long ago...\n(around 1400year a.c.)\na')
#--------------------------------------------------------#

#ITEMS PRESETS-->
HealingPotionI=item('Healing Potion',20, '   Heals 20HP', 10, 1)

#WEAPONS PRESETS -->
Stick=weapon('Stick', 0, 10, 20, 0)
Cane=weapon('Cane',10,11,21, 5)
IronSword=weapon('Iron Sword', 70,40,60, 35)
Knife=weapon('Knife',30,40,50, 15)
MimicTeeth=weapon('Mimic Teeth',0,30,50,0)

#ARMOR PRESETS -->
SlaveRobe=armor('Slaves Robe', 0, 1,0)
IronArmor=armor('Iron Armor', 50,2,25)
MimicSkin=armor('Mimic skin', 0,2,0)

#USER SPECS -->
user=Character('user',100,100, Stick, SlaveRobe)
user.hp=min(user.hp,100)

#ENEMY PRESETS -->
goblin1=Character('Goblin',100,20, Stick, SlaveRobe)
goblin1.hp=min(goblin1.hp,100)
Mimic = Character('Mimic',200,90,MimicTeeth,MimicSkin)

#--------------------------------------------------------#

#def base():
#global running, user, rcount, inventory
while running:
    enemy=Character(None,None,None,None,None,)
    if rcount == 0:
        print('____________')
        print('GAME STARTS')
        print('------------')
        user = Character('User',100, 100, Stick, SlaveRobe)
        user.hp = min(user.hp, 100)
        steps_list=[]
    else:
        print('___________________')
        print('recursion happened')
    print("Money: ", user.money)
    print('Weapon:', user.weapon.name,'- damage:', user.weapon.dmg_min,'-', user.weapon.dmg_max)
    print('Armor:',user.armor.name, '- defence:', user.armor.defence)
    print('HP:', user.hp)
    print('LVL', user_lvl)
    print("Recursion count:", rcount)
    if 'Healing Potion' in inventory:
        print('press 5 to use Healing potion')
    print('press 9 to show inventory')
    print('press 0 to exit')
    print('choose a way')
    print('1.right')
    print('2.left')
    rcount +=1

    usr_choose = minput()


    if usr_choose==1:
        steps_list.append(1)
        num_events = 1
        event=random.randint(1,num_events)
        if event==1:
            enemy=EnemyGen(enemy)
            battle(enemy,user)

    if usr_choose==2:
        steps_list.append(2)
        num_events = 2
        event = random.randint(1, num_events)
        if event == 1:
            shop(user)
            continue
        elif event==(2):
            chestevent(user)