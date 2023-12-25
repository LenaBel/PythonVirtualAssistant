from Assistant import Assistant
from alarm.AlarmManager import AlarmManager, Task

if __name__ == '__main__':
    alarmManager = AlarmManager()
    assistant = Assistant(alarmManager)
    assistant.start_virtual_assistant()
    alarmManager.save_alarms_to_file()
    