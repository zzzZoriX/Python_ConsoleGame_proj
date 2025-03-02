import data
from player import *
from enemy import *

# другие действия #
def open_inventory(): pass
def check_stats(): pass

# игровые функции #
def battle_cycle() -> int:
    while(data.enemy_stats[1] > 0 and data.player_stats[1] > 0):
        print(f"\nздоровье врага: {data.enemy_stats[1]}\nваше здоровье: {data.player_stats[1]}\nваша энергия: {data.player_stats[4]}\n")

        print("выберите действие:\n  attack (-2 энергии)\n  inventory\n  skip (+1 енергия)\n  check stats\n  exit")
        action = input("> ").replace(' ', '')

        while(action not in data.player_actions):
            print("неизвестное действие!\n")
            action = input("> ").replace(' ', '')
        
        if(action == data.player_actions[0]): # атака
            player_attack()
            enemy_defends()
        
        elif(action == data.player_actions[1]): # просмотреть статы
            print(f"""
                  HP: {data.player_stats[1]}
                  урон: {data.player_stats[0]}
                  уровень: {data.player_stats[3]}
                  баланс: {data.player_stats[2]}
                  """)
            continue
            
        elif(action == data.player_actions[2]): # инвентарь
            continue
        
        elif(action == data.player_actions[3]): # скип
            if(data.player_stats[4] < 10):
                data.player_stats[4] += 1    
            print()
        
        elif(action == data.player_actions[4]): # выход
            print("выход...")
            return 2
        
        
        print("защититься?")
        action = input("(Y / N): ")
        
        if(enemy_attack() and action.upper() == 'Y'):
            player_defends() 
            
    return 0
    
    
def check_hp() -> int:
    if(data.player_stats[1] <= 0):
        print("вы проиграли")
        return 0
        
    elif(data.enemy_stats[1] <= 0):
        print("враг побежден")
        enemy_defeated()
        return 1