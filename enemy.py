import data
import random

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
    print("враг не защитился")

def enemy_defeated():
    data.player_stats[2] += data.enemy_stats[5]
    
def enemy_buff(): pass