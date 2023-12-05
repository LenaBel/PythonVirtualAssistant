import datetime

from abc import abstractmethod
from pathlib import Path
from typing import Dict, Iterable, List


from alarm.Alarm import *


class AbstractStorage(object):
    """ Определяет интерфейс хранилища будильников. """


    @abstractmethod
    def get_all(self) -> Iterable[Alarm]:
        """ Возвращает набор всех будильников из хранилища. """
        raise NotImplementedError


    @abstractmethod
    def put_all(self, alarm: Alarm):
        """ Складывает будильники в хранилище. """
        raise NotImplementedError


class FileStorage(AbstractStorage):
    """ Реализация хранилища в файле. """


    def __init__(self, path: Path, delimiter: str = ';;'):
        self.__path = path
        self.__delimiter = delimiter

        # NOTE: Если файла хранилища нет по указанному пути, создадим его.
        if not self.__path.exists():
            self.__path.touch()


    def get_all(self) -> Dict[int, Alarm]:
        # NOTE: Открываем файл хранилища на чтение.
        dictionary: Dict[int, Alarm] = {}
        with self.__path.open('r') as my_file:
            # NOTE: Читаем файл построчно и для каждой строки формируем будильник.
            for line in my_file:
                alarm: Alarm = self.__make_alarm(line.removesuffix('\n'))
                dictionary[alarm.alarm_id] = alarm

        return dictionary


    def set_all(self, alarms: Iterable[Alarm]):
        lines = [self.__make_line(a) for a in alarms]
        self.__path.write_text('\n'.join(lines))


    def __make_line(self, alarm: Alarm) -> str:
        fields: List[str] = [str(alarm.alarm_id), alarm.name, alarm.is_on, alarm.time]
        return f'{type(alarm).__name__}|{self.__delimiter.join(fields)}' # TODO Test

  
    def __make_alarm(self, line: str) -> Alarm:
        data = line.split('|')

        alarm_id, name, is_on, time = data.split(self.__delimiter)
        return Alarm(int(alarm_id), name, is_on, datetime.fromisoformat(time))







