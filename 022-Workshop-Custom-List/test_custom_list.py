import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        self.cl = CustomList(1, 2, 3)

    def test_append_extend_insert_return_the_list(self):
        self.assertEqual(self.cl.append(4), [1, 2, 3, 4])
        self.assertEqual(self.cl.extend((5, 6)), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.cl.insert(0, 0), [0, 1, 2, 3, 4, 5, 6])

    def test_remove_and_get(self):
        self.assertEqual(self.cl.get(1), 2)
        self.assertEqual(self.cl.remove(0), 1)
        self.assertEqual(self.cl.size(), 2)
        with self.assertRaises(IndexError):
            self.cl.get(10)
        with self.assertRaises(TypeError):
            self.cl.remove("0")

    def test_pop_and_clear(self):
        self.assertEqual(self.cl.pop(), 3)
        self.cl.clear()
        self.assertEqual(self.cl.size(), 0)
        with self.assertRaises(IndexError):
            self.cl.pop()

    def test_index_count_reverse_copy(self):
        self.cl.append(2)
        self.assertEqual(self.cl.index(2), 1)
        self.assertEqual(self.cl.count(2), 2)
        self.assertEqual(self.cl.reverse(), [2, 3, 2, 1])
        copy = self.cl.copy()
        copy.append(99)
        self.assertEqual(self.cl.size(), 4)

    def test_add_first(self):
        self.cl.add_first(0)
        self.assertEqual(self.cl.get(0), 0)

    def test_dictionize(self):
        self.assertEqual(CustomList("a", 1, "b", 2).dictionize(), {"a": 1, "b": 2})
        self.assertEqual(self.cl.dictionize(), {1: 2, 3: " "})

    def test_move(self):
        self.assertEqual(self.cl.move(2), [3, 1, 2])
        with self.assertRaises(ValueError):
            self.cl.move(5)

    def test_sum_counts_length_of_non_numbers(self):
        self.assertEqual(CustomList(1, 2.5, "abc", [1, 2]).sum(), 8.5)

    def test_over_and_underbound(self):
        cl = CustomList(5, "abcdefg", 1, "ab")
        self.assertEqual(cl.overbound(), 1)
        self.assertEqual(cl.underbound(), 2)
        with self.assertRaises(ValueError):
            CustomList().overbound()


if __name__ == "__main__":
    unittest.main()
