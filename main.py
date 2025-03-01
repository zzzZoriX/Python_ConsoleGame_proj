import data 
from enemy import *
from player import *
from game_main import *

while(True):
    battle_cycle()
    
    if(check_hp()): continue
    else: break