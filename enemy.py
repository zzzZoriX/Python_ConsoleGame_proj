import data, random
from player import lvl_up

# дейдействия противника #
def enemy_attack() -> bool:
    if((random.randint(0, 100) / 100) < data.enemy_stats[3]):
        data.player_stats[1] -= data.enemy_stats[0]
        print("\nвраг атаковал")
        return True
    
def enemy_defends(): 
    if((random.randint(0, 100) / 100) < data.enemy_stats[4]):
        data.enemy_stats[1] += data.player_stats[0] * data.enemy_stats[2]
        print("враг защитился\n")
        return
    print("враг не защитился\n")

def enemy_defeated():
    data.player_stats[2] += data.enemy_stats[5]
    data.player_stats[9] += data.enemy_stats[6]
    
    if(data.player_stats[9] >= data.player_stats[8]): # если опыта хватает для апа лвла
        print("уровень повышен!\n")
        lvl_up()
    
def enemy_buff():
    data.enemy_stats[1] = data.enemy_stats[7]
    
    data.enemy_stats[0] = float(int(data.enemy_stats[0] * 1.25))
    data.enemy_stats[1] = float(int(data.enemy_stats[1] * 1.5))
    data.enemy_stats[6] = round(data.enemy_stats[6] * data.exp_multi_for_enemy, 2)
    data.enemy_stats[5] = round(data.enemy_stats[5] * data.exp_multi_for_enemy, 2)
    
    data.enemy_stats[7] = data.enemy_stats[1]