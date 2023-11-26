from typing import Dict, Iterable
from alarm.Alarm import Alarm


class AlarmManager:
    ''' Менеджер будильников'''


    def __init__(self):
        self.__alarms: Dict[int, Alarm] = {}


    def add_alarm(self, alarm: Alarm):
        '''Добавляет будильник'''
        #todo get id in here?
        if alarm not in self.__alarms.values:
            self.__alarms[alarm.alarm_id] = alarm


    def remove_alarm(self, alarm_id: int):
        ''' Удаляет будильник '''
        if alarm_id in self.__alarms.keys:
            del self.__alarms[alarm_id]
            

    def get_alarm(self, alarm_id: int) -> Alarm:
        ''' Возвращает будильник '''
        if alarm_id in self.__alarms.keys:
            return self.__alarms[alarm_id]
        else:
            return None


    def get_alarms(self) -> Iterable[Alarm]:
        ''' Возвращает список будильников '''
        return self.__alarms.values()
        


    def off_alarm(self, alarm_id: int):
        ''' Отключает будильник '''
        if alarm_id in self.__alarms.keys:
            self.__alarms[alarm_id].is_on = False


    def on_alarm(self, alarm_id: int):
        ''' Включает будильник '''
        if alarm_id in self.__alarms.keys:
            self.__alarms[alarm_id].is_on = True


    def call_alarm(self):
        ''' Звонит в будильник '''
        print('динь-дон!')
