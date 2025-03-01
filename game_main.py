import data
from player import *
from enemy import *

# другие действия #
def open_inventory(): pass
def check_stats(): pass

# игровые функции #
def battle_cycle():
    while(data.enemy_hp > 0 and data.player_hp > 0):
        print(f"\nздоровье врага: {data.enemy_hp}\nваше здоровье: {data.player_hp}\nваша энергия: {data.player_energy}\n")

        print("выберите действие:\n  attack (-2 энергии)\n  inventory\n  skip (+1 енергия)\n  check stats")
        action = input("> ")
        while(action not in data.player_actions):
            print("неизвестное действие!\n")
            action = input("> ")
        
        if(action == data.player_actions[0]): # атака
            player_attack()
            enemy_defends()
        
        elif(action == data.player_actions[1]): # просмотреть статы
            print(f"""
                  HP: {data.player_hp}
                  урон: {data.player_damage}
                  уровень: {data.player_exp}
                  баланс: {data.player_balance}
                  """)
            continue
            
        elif(action == data.player_actions[3]):
            if(data.player_energy < 10):
                data.player_energy += 1
            print()
            
        elif(action == data.player_actions[2]): # инвентарь
            continue
        
        
        print("защититься?")
        action = input("(Y / N): ")
        
        if(enemy_attack() and action.upper() == 'Y'):
            player_defends() 
    
    
def check_hp() -> int:
    if(data.player_hp <= 0):
        print("вы проиграли")
        return 0
        
    elif(data.enemy_hp <= 0):
        print("враг побежден")
        enemy_defeated()
        return 1