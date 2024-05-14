from abc import ABC, abstractmethod


# Receiver
class HouseholdAppliance:
    def __init__(self, name):
        self.name = name
        self.state = False

    def turn_on(self):
        self.state = True
        print(f"{self.name} включено")

    def turn_off(self):
        self.state = False
        print(f"{self.name} вимкнено")


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, appliance):
        self.appliance = appliance

    def execute(self):
        self.appliance.turn_on()

    def undo(self):
        self.appliance.turn_off()


class TurnOffCommand(Command):
    def __init__(self, appliance):
        self.appliance = appliance

    def execute(self):
        self.appliance.turn_off()

    def undo(self):
        self.appliance.turn_on()


# Invoker
class SmartRoomController:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        self.commands.append(command)
        command.execute()

    def undo_last_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()


if __name__ == "__main__":
    light = HouseholdAppliance("Світло")
    boiler = HouseholdAppliance("Котел")
    conditioner = HouseholdAppliance("Кондиціонер")
    kettle = HouseholdAppliance("Чайник")

    room_controller = SmartRoomController()

    turn_on_light = TurnOnCommand(light)
    turn_on_boiler = TurnOnCommand(boiler)
    turn_on_conditioner = TurnOnCommand(conditioner)
    turn_on_kettle = TurnOnCommand(kettle)
    turn_off_kettle = TurnOffCommand(kettle)

    room_controller.execute_command(turn_on_light)
    room_controller.execute_command(turn_on_boiler)
    room_controller.execute_command(turn_on_conditioner)
    room_controller.execute_command(turn_on_kettle)
    room_controller.execute_command(turn_off_kettle)

    room_controller.undo_last_command()
