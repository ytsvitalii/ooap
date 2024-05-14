from datetime import datetime


class Interpreter:
    def interpret(self, date_str):
        pass


class MMDDYYYYInterpreter(Interpreter):
    def interpret(self, date_str):
        return datetime.strptime(date_str, "%m-%d-%Y")


class DDMMYYYYInterpreter(Interpreter):
    def interpret(self, date_str):
        return datetime.strptime(date_str, "%d-%m-%Y")


class YYYYMMDDInterpreter(Interpreter):
    def interpret(self, date_str):
        return datetime.strptime(date_str, "%Y-%m-%d")


class DateParser:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def parse(self, date_str):
        return self.interpreter.interpret(date_str)


class UserInterface:
    def __init__(self):
        self.parsers = {
            "MM-DD-YYYY": DateParser(MMDDYYYYInterpreter()),
            "DD-MM-YYYY": DateParser(DDMMYYYYInterpreter()),
            "YYYY-MM-DD": DateParser(YYYYMMDDInterpreter())
        }

    def get_date(self, format_str: str):
        date_str = input(f"Введіть дату у форматі {format_str}: ")
        parser = self.parsers.get(format_str)
        if parser:
            return parser.parse(date_str)
        else:
            raise ValueError("Невідомий формат дати")


if __name__ == "__main__":
    ui = UserInterface()
    format_str = input("Виберіть формат дати (MM-DD-YYYY, DD-MM-YYYY, YYYY-MM-DD): ")
    try:
        date = ui.get_date(format_str)
        print("Введена дата:", date)
    except ValueError as e:
        print(e)
