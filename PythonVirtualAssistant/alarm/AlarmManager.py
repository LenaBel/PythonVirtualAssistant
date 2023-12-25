import subprocess
from pathlib import Path
from typing import Dict, Iterable
from alarm.Alarm import Alarm
from alarm.Storage import FileStorage
from datetime import datetime, timedelta
from threading import Lock, Thread


import time
import platform, os
from win10toast import ToastNotifier
import asyncio

class AlarmManager:
    ''' Менеджер будильников'''


    def __push(self, title, message):
        plt = platform.system()
        if plt == "Linux":
            subprocess.call('notify-send', title, message)
        elif plt == "Windows":
            ToastNotifier().show_toast(title, message)
            return
        else:
            return

    def __call_alarm(self, alarm: Alarm):
        if alarm.alarm_id in self.__alarms.keys() and self.__alarms[alarm.alarm_id].is_on:
            self.__push(alarm.name, 'ДИНЬ-ДОН! ЗВОНИТ БУДИЛЬНИК')
            self.__alarms[alarm.alarm_id].is_on = False


    def set_call(self, alarm: Alarm):
        now = datetime.now()
        delta: timedelta = alarm.time - now
        time.sleep(delta.total_seconds())
        if alarm.alarm_id in self.__alarms.keys() and self.__alarms[alarm.alarm_id].is_on:
            self.__push(alarm.name, 'ДИНЬ-ДОН! ЗВОНИТ БУДИЛЬНИК')
            self.__alarms[alarm.alarm_id].is_on = False


    def __check_alarms(self):
            if self.__alarms.keys().__len__() > 0:
                now = datetime.now()

                for alarm in self.__alarms.values():
                    if alarm.is_on and now < alarm.time:
                        try:
                            task = Task(self, alarm)
                            tr = Thread(target=task)
                            tr.start()
                        except:
                            pass


    def __init__(self):
        self.__fileStorage: FileStorage = FileStorage(Path('storage.txt'))
        self.__alarms: Dict[int, Alarm] = self.__fileStorage.get_all()
        self.__check_alarms()


    def __add_alarm(self, alarm: Alarm):
        '''Добавляет будильник'''
        try:
            id: int = 0
            if len(self.__alarms.keys()) > 0:
                id = int(list(self.__alarms.keys())[-1]) + 1
            alarm.alarm_id = id
            self.__alarms[alarm.alarm_id] = alarm
            if datetime.now() < alarm.time:
                try:
                    task = Task(self, alarm)
                    tr = Thread(target=task)
                    tr.start()
                except:
                    pass
        except Exception as ex:
            print(ex)


    def __remove_alarm(self, alarm_id: int):
        ''' Удаляет будильник '''
        if alarm_id in self.__alarms.keys():
            del self.__alarms[alarm_id]
            

    def __get_alarm(self, alarm_id: int) -> Alarm | None:
        ''' Возвращает будильник '''
        if alarm_id in self.__alarms.keys():
            return self.__alarms[alarm_id]
        else:
            return None


    def __get_alarms(self) -> Iterable[Alarm]:
        ''' Возвращает список будильников '''
        return self.__alarms.values()
        

    def __off_alarm(self, alarm_id: int):
        ''' Отключает будильник '''
        if alarm_id in self.__alarms.keys():
            self.__alarms[alarm_id].is_on = False


    def __on_alarm(self, alarm_id: int):
        ''' Включает будильник '''
        if alarm_id in self.__alarms.keys():
            self.__alarms[alarm_id].is_on = True


    def __call_alarm(self):
        ''' Звонит в будильник '''
        print('динь-дон! :)')


    def save_alarms_to_file(self):
        '''сохранение будильников '''
        if (self.__alarms.__len__() > 0):
            self.__fileStorage.set_all(self.__alarms.values())


    def start_manage_alarms(self):
        print('Запущен менеджер будильников')
        while True:
            time.sleep(1)
            operation = input('''Выберите номер операции: 
                     1. Показать список будильников
                     2. Добавить будильник
                     3. Удалить будильник
                     4. Показать информацию о будильнике по ID
                     5. Позвонить в звоночек :-)
                     6. Вернуться в основное меню виртуального помощника \n''')

            if operation == '1':
                print(self.__get_alarms())

            elif operation == '2':
                try:
                    al_name = input('Введите имя будильника: ')
                    al_dtime = datetime.strptime(input('Время будильника в формате месяц/день/год(последние 2 цифры) час:мин:сек. Например, 01/19/24 13:55:26: '), '%m/%d/%y %H:%M:%S')
                    new_alarm = Alarm(al_name, al_dtime)
                    self.__add_alarm(new_alarm)
                except ValueError:
                    print('Неверный ввод')
                    continue

            elif operation == '3':
                try:
                    del_id = int(input("Введите ID будильника: "))
                    self.__remove_alarm(del_id)
                except ValueError:
                    print('Неверный ввод, нужно ввести число')
                    continue

            elif operation == '4':
                try:
                    one_id = int(input("Введите ID будильника: "))
                    print(self.__get_alarm(one_id))
                except ValueError:
                    print('Неверный ввод, нужно ввести число')
                    continue

            elif operation == '5':
                self.__call_alarm()

            elif operation == '6':
                break

            else:
                print("Неверный ввод")

            '''
            elif operation == '4':
                try:
                    off_id = int(input("Введите ID будильника: "))
                    self.__off_alarm(off_id)
                except ValueError:
                    print('Неверный ввод, нужно ввести число')
                    continue

            elif operation == '5':
                try:
                    on_id = int(input("Введите ID будильника: "))
                    self.__on_alarm(on_id)
                except ValueError:
                    print('Неверный ввод, нужно ввести число')
                    continue
            '''

class Task(object):
    def __init__(self, alarm_manager: AlarmManager, alarm: Alarm):
        self.__alarm_manager = alarm_manager
        self.__alarm = alarm

    def __call__(self):
        lock = Lock()
        with lock:
            self.__alarm_manager.set_call(self.__alarm)
