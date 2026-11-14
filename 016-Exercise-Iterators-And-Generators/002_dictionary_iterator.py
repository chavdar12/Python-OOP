class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.items = list(dict_obj.items())
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.items):
            raise StopIteration
        self.count += 1
        return self.items[self.count - 1]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
