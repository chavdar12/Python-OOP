import unittest

from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld


class TestDVD(unittest.TestCase):
    def test_from_date(self):
        dvd = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
        self.assertEqual((dvd.id, dvd.name, dvd.creation_year, dvd.creation_month), (2, "The Croods 2", 2020, "December"))

    def test_repr(self):
        self.assertEqual(repr(DVD("Black Widow", 1, 2020, "April", 18)),
                         "1: Black Widow (April 2020) has age restriction 18. Status: not rented")


class TestMovieWorld(unittest.TestCase):
    def setUp(self):
        self.world = MovieWorld("Shop")
        self.john = Customer("John", 16, 1)
        self.anna = Customer("Anna", 55, 2)
        self.adult = DVD("Black Widow", 1, 2020, "April", 18)
        self.kids = DVD("Croods", 2, 2020, "December", 3)
        for customer in (self.john, self.anna):
            self.world.add_customer(customer)
        for dvd in (self.adult, self.kids):
            self.world.add_dvd(dvd)

    def test_capacities(self):
        for i in range(20):
            self.world.add_customer(Customer(str(i), 20, i + 10))
            self.world.add_dvd(DVD(str(i), i + 10, 2020, "May", 0))
        self.assertEqual(len(self.world.customers), MovieWorld.customer_capacity())
        self.assertEqual(len(self.world.dvds), MovieWorld.dvd_capacity())

    def test_rent_dvd(self):
        self.assertEqual(self.world.rent_dvd(1, 1), "John should be at least 18 to rent this movie")
        self.assertEqual(self.world.rent_dvd(2, 1), "Anna has successfully rented Black Widow")
        self.assertEqual(self.world.rent_dvd(2, 1), "Anna has already rented Black Widow")
        self.assertEqual(self.world.rent_dvd(1, 1), "DVD is already rented")

    def test_return_dvd(self):
        self.world.rent_dvd(2, 1)
        self.assertEqual(self.world.return_dvd(1, 1), "John does not have that DVD")
        self.assertEqual(self.world.return_dvd(2, 1), "Anna has successfully returned Black Widow")
        self.assertFalse(self.adult.is_rented)

    def test_repr(self):
        self.world.rent_dvd(1, 2)
        self.assertEqual(repr(self.world).splitlines()[0], "1: John of age 16 has 1 rented DVD's (Croods)")


if __name__ == "__main__":
    unittest.main()
