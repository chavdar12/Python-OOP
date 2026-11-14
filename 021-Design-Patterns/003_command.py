from abc import ABC, abstractmethod


class Window:
    def exit(self):
        return "Window closed"


class Document:
    def __init__(self, name):
        self.name = name

    def save(self):
        return f"{self.name} saved"


class Command(ABC):
    @abstractmethod
    def execute(self): ...


class SaveCommand(Command):
    def __init__(self, document):
        self.document = document

    def execute(self):
        return self.document.save()


class ExitCommand(Command):
    def __init__(self, window):
        self.window = window

    def execute(self):
        return self.window.exit()


class ToolbarDocument:
    def __init__(self, command):
        self.command = command

    def click(self):
        return self.command.execute()


class MenuItem(ToolbarDocument):
    pass


class KeyboardShortcut:
    def __init__(self, command):
        self.command = command

    def keypress(self):
        return self.command.execute()


if __name__ == "__main__":
    save = SaveCommand(Document("notes.txt"))
    print(ToolbarDocument(save).click(), KeyboardShortcut(save).keypress(), sep="\n")
    print(MenuItem(ExitCommand(Window())).click())
