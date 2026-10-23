import unittest

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo


class TestAnimalsAndWorkers(unittest.TestCase):
    def test_money_for_care(self):
        self.assertEqual([Lion("a", "M", 1).money_for_care, Tiger("a", "M", 1).money_for_care,
                          Cheetah("a", "M", 1).money_for_care], [50, 45, 60])

    def test_repr(self):
        self.assertEqual(repr(Lion("Simba", "Male", 4)), "Name: Simba, Age: 4, Gender: Male")
        self.assertEqual(repr(Vet("Peter", 40, 300)), "Name: Peter, Age: 40, Salary: 300")


class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo("Zootopia", 300, 2, 2)

    def test_add_animal(self):
        self.assertEqual(self.zoo.add_animal(Lion("Simba", "Male", 4), 100), "Simba the Lion added to the zoo")
        self.assertEqual(self.zoo.add_animal(Tiger("Zuba", "Male", 3), 1000), "Not enough budget")

    def test_add_animal_without_space_reports_space_first(self):
        self.zoo.add_animal(Lion("a", "M", 1), 10)
        self.zoo.add_animal(Lion("b", "M", 1), 10)
        self.assertEqual(self.zoo.add_animal(Lion("c", "M", 1), 1000), "Not enough space for animal")

    def test_hire_and_fire(self):
        self.assertEqual(self.zoo.hire_worker(Keeper("John", 26, 100)), "John the Keeper hired successfully")
        self.zoo.hire_worker(Vet("Peter", 40, 300))
        self.assertEqual(self.zoo.hire_worker(Caretaker("Bill", 21, 68)), "Not enough space for worker")
        self.assertEqual(self.zoo.fire_worker("John"), "John fired successfully")
        self.assertEqual(self.zoo.fire_worker("John"), "There is no John in the zoo")

    def test_pay_workers(self):
        self.zoo.hire_worker(Keeper("John", 26, 100))
        self.assertEqual(self.zoo.pay_workers(), "You payed your workers. They are happy. Budget left: 200")
        self.zoo.hire_worker(Vet("Peter", 40, 300))
        self.assertEqual(self.zoo.pay_workers(), "You have no budget to pay your workers. They are unhappy")

    def test_tend_animals_and_profit(self):
        self.zoo.add_animal(Lion("Simba", "Male", 4), 280)
        self.assertEqual(self.zoo.tend_animals(), "You have no budget to tend the animals. They are unhappy.")
        self.zoo.profit(100)
        self.assertEqual(self.zoo.tend_animals(), "You tended all the animals. They are happy. Budget left: 70")

    def test_statuses(self):
        self.zoo.add_animal(Lion("Simba", "Male", 4), 10)
        self.zoo.hire_worker(Vet("Peter", 40, 300))
        self.assertEqual(self.zoo.animals_status(),
                         "You have 1 animals\n----- 1 Lions:\nName: Simba, Age: 4, Gender: Male\n"
                         "----- 0 Tigers:\n----- 0 Cheetahs:")
        self.assertEqual(self.zoo.workers_status(),
                         "You have 1 workers\n----- 0 Keepers:\n----- 0 Caretakers:\n"
                         "----- 1 Vets:\nName: Peter, Age: 40, Salary: 300")


if __name__ == "__main__":
    unittest.main()
