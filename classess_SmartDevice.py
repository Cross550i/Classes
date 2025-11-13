class SmartDevice:
    def activate(self) -> None:
        pass

class SmartLight(SmartDevice):
    def activate(self):
        print("Свет включен, яркость 80%")
        self.brightness = 80

    def deactivate(self):
        print("Свет выключен")

class Thermostat(SmartDevice):
    def activate(self):
        print("Термостат включен (тем-ра 25')")
        self.temperature = 25

    def deactivate(self):
        print("Термостат выключен")


class MorningRoutine:
    def __init__(self) -> None:
         self.devices = []

    def add_device(self, device):
        self.devices.append(device)


    def start_morning(self):
        print("Запуск утреннего режима")
        for device in self.devices:
            device.activate()
            print("Режим 'Доброе утро' активирован")


routine = MorningRoutine()
routine.add_device(SmartLight())
routine.add_device(Thermostat())
routine.start_morning()







