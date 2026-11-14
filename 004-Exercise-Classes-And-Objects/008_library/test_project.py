import unittest

from project.library import Library
from project.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(12, "Peter")
        self.library = Library()
        self.library.books_available["J.K.Rowling"] = ["Chamber", "Prisoner"]

    def test_get_book(self):
        self.assertEqual(self.user.get_book("J.K.Rowling", "Chamber", 17, self.library),
                         "Chamber successfully rented for the next 17 days!")
        self.assertEqual(self.library.books_available["J.K.Rowling"], ["Prisoner"])
        self.assertEqual(self.library.rented_books, {"Peter": {"Chamber": 17}})
        self.assertEqual(self.user.books, ["Chamber"])

    def test_get_two_books_keeps_both_records(self):
        self.user.get_book("J.K.Rowling", "Chamber", 17, self.library)
        self.user.get_book("J.K.Rowling", "Prisoner", 5, self.library)
        self.assertEqual(self.library.rented_books, {"Peter": {"Chamber": 17, "Prisoner": 5}})

    def test_get_rented_book(self):
        self.user.get_book("J.K.Rowling", "Chamber", 17, self.library)
        self.assertEqual(User(13, "Anna").get_book("J.K.Rowling", "Chamber", 3, self.library),
                         'The book "Chamber" is already rented and will be available in 17 days!')

    def test_return_book(self):
        self.assertEqual(self.user.return_book("J.K.Rowling", "Chamber", self.library),
                         "Peter doesn't have this book in his/her records!")
        self.user.get_book("J.K.Rowling", "Chamber", 17, self.library)
        self.user.return_book("J.K.Rowling", "Chamber", self.library)
        self.assertEqual(self.user.books, [])
        self.assertIn("Chamber", self.library.books_available["J.K.Rowling"])
        self.assertEqual(self.library.rented_books["Peter"], {})

    def test_info_and_str(self):
        self.user.books = ["b", "a"]
        self.assertEqual(self.user.info(), "a, b")
        self.assertEqual(str(self.user), "12, Peter, ['b', 'a']")


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.user = User(12, "Peter")

    def test_add_user(self):
        self.assertIsNone(self.library.add_user(self.user))
        self.assertEqual(self.library.add_user(self.user), "User with id = 12 already registered in the library!")

    def test_remove_user(self):
        self.assertEqual(self.library.remove_user(self.user), "We could not find such user to remove!")
        self.library.add_user(self.user)
        self.library.rented_books["Peter"] = {"x": 1}
        self.library.remove_user(self.user)
        self.assertEqual(self.library.user_records, [])
        self.assertNotIn("Peter", self.library.rented_books)

    def test_change_username_finds_any_user(self):
        self.library.add_user(User(1, "First"))
        self.library.add_user(self.user)
        self.assertEqual(self.library.change_username(12, "George"),
                         "Username successfully changed to: George for userid: 12")
        self.assertEqual(self.user.username, "George")
        self.assertIs(self.library.user_records[1], self.user)

    def test_change_username_errors(self):
        self.library.add_user(self.user)
        self.assertEqual(self.library.change_username(2, "Igor"), "There is no user with id = 2!")
        self.assertEqual(self.library.change_username(12, "Peter"),
                         "Please check again the provided username - it should be different than the username used so far!")

    def test_change_username_moves_rented_books(self):
        self.library.add_user(self.user)
        self.library.rented_books["Peter"] = {"x": 1}
        self.library.change_username(12, "George")
        self.assertEqual(self.library.rented_books, {"George": {"x": 1}})


if __name__ == "__main__":
    unittest.main()
