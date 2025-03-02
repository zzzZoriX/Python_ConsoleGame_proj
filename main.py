from game_main import *
import win32api

file_name = "save_data.txt"

"""
структура файла:
p\
здоровье_игрока урон_игрока энергия_игрока поглощаемый_урон_игрока стоймость_атаки стоймость_защиты баланс уровень
предметы инвенторя
e\
здоровье_врага урон_врага отражаемый_урон_врага шанс_атаки_врага шанс_защиты_врага колво_выпадающих_монет
"""


def save_data_():
    try:
        save_file_stream = open(file_name, "w", encoding='utf8')
    except Exception as err:
        print("ошибка - ", err)

    data_buffer = "p\\\n"
    for state in data.player_stats:
        data_buffer = data_buffer + str(state) + ' '

    save_file_stream.write(data_buffer)

    save_file_stream.close()

def load_data_(): pass

def exit_():
    print("сохраниться?")
    answer = input("(Y / N): ")

    if(answer.upper() == 'Y'):
        save_data_()

def main_():
    while(True):
        if(battle_cycle() == 2):
            exit_()
            return

        if(check_hp()): continue
        else: break


main_()