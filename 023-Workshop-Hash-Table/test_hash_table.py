import unittest

from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_example(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 25
        self.assertEqual(table.get("name"), "Peter")
        self.assertEqual(table["age"], 25)
        self.assertEqual(len(table), 4)

    def test_overwrites_existing_key(self):
        table = HashTable()
        table.add("a", 1)
        table.add("a", 2)
        self.assertEqual(table["a"], 2)

    def test_doubles_when_full_and_keeps_data(self):
        table = HashTable()
        keys = [f"key{i}" for i in range(10)]
        for i, key in enumerate(keys):
            table[key] = i
        self.assertGreaterEqual(len(table), 16)
        for i, key in enumerate(keys):
            self.assertEqual(table[key], i)

    def test_missing_key_raises(self):
        with self.assertRaises(KeyError):
            HashTable().get("missing")


if __name__ == "__main__":
    unittest.main()
