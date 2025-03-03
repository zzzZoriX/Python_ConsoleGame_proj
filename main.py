from game_main import *
import os
import ctypes

file_name = "save_data.txt"

"""
p\ <- от слова player
урон_игрока хп_игрока баланс_игрока уровень_игрока енергия_игрока отражаемый_урон_игрока стоймость_защиты стоймость_атавки опыт_для_некст_уровня текущий_опыт
предметы инвенторя
e\ <- от слова enemy
урон_врага хп_врага отражаемый_урон_врага шанс_атаки_врага шанс_защиты_врага деньги_выпадающие_с_врага дроп_опыт полное_здоровье
"""    


def set_hidden__(attrs, hidden = True):
    if(hidden):
        ctypes.windll.kernel32.SetFileAttributesW(file_name, attrs | 0x02) # скрываем
    else:
        ctypes.windll.kernel32.SetFileAttributesW(file_name, attrs & ~0x02) # показываем


def save_data_(): 
    try:
        save_file_stream = open(file_name, "w", encoding='utf8')
        
        attrs = ctypes.windll.kernel32.GetFileAttributesW(file_name)
        set_hidden__(attrs, False)
        
    except Exception as err:
        print("ошибка - ", err)
    
    # стата игрока
    data_buffer = 'p\\\n'
    for i in range(0, len(data.player_stats)):
        data_buffer = data_buffer + str(data.player_stats[i]) + ('\n' if i == 9 else ' ') # если data.player_stats[i] - последний элемент, то добавляем перевод строки
    
    # стата врага
    data_buffer = data_buffer + 'e\\\n'
    for i in range(0, len(data.enemy_stats)):
        data_buffer = data_buffer + str(data.enemy_stats[i]) + (' ' if i != 7 else '') # если data.enemy_stats[i] - не последний элемент, то добавляем пробел
    
    save_file_stream.write(data_buffer)
    
    save_file_stream.close()
    
    set_hidden__(attrs)
    
    
def load_data_():
    try:
        save_file_stream = open(file_name, "r", encoding='utf8')
        
        attrs = ctypes.windll.kernel32.GetFileAttributesW(file_name)
        set_hidden__(attrs, False)
    
    except FileNotFoundError:
        create_save_file = open(file_name, "w", encoding='utf8')
        create_save_file.close()
        return    
    
    except Exception as err:
        print("ошибка - ", err)
        
    file_size = os.stat(file_name)
    if(not file_size.st_size): return # если файл сохранения пустой
        
    data_buffer = ' '.join(save_file_stream.read().split('\n')).split()
    save_file_stream.close()
    
    i = 1 # дата-буффер
    k = 0 # инедкс массивов статов
    current_is_enemy_data = False
    while(i != len(data_buffer)):
        if(not current_is_enemy_data and k < len(data.player_stats)):
            data.player_stats[k] = float(data_buffer[i])
            k += 1
        
        elif(current_is_enemy_data):
            data.enemy_stats[k] = float(data_buffer[i])
            k += 1
        
        if(data_buffer[i] == 'e\\'):
            k = 0
            current_is_enemy_data = True

        i += 1
        
    set_hidden__(attrs)
    

def exit_():
    print("созранить текущий прогресс?")
    answer = input("(Y / N): ")
    
    if(answer.upper() == 'Y'):
        save_data_()
    
    
def main_():
    load_data_()
    
    while(True):
        if(battle_cycle() == 2):
            exit_()
            return
        
        if(not check_hp()):
            break


main_()