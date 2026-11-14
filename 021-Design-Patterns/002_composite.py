class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_parent):
        if self.parent:
            self.parent.children.remove(self)
        new_parent.add_child(self)

    def delete(self):
        if self.parent:
            self.parent.children.remove(self)
            self.parent = None

    def get_path(self):
        if self.parent is None:
            return self.name
        return f"{self.parent.get_path()}/{self.name}"


class File(Component):
    pass


class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


if __name__ == "__main__":
    root = Folder("root")
    docs = Folder("docs")
    root.add_child(docs)
    report = File("report.txt")
    docs.add_child(report)
    print(report.get_path())
