import data
import random

# дейдействия противника #
def enemy_attack() -> bool:
    if((random.randint(0, 100) / 100) < data.enemy_atack_chance):
        data.player_hp -= data.enemy_damage
        print("\nвраг атаковал")
        return True
    
def enemy_defends(): 
    if((random.randint(0, 100) / 100) < data.enemy_defends_chance):
        data.enemy_hp += data.player_damage * data.enemy_absorbed_damage_proc
        print("враг защитился\n")
        return
    print("враг не защитился")

def enemy_defeated():
    data.player_balance += data.drops_money