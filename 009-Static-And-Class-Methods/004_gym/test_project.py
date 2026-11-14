import unittest

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

CLASSES = (Customer, Equipment, ExercisePlan, Subscription, Trainer)


class TestGym(unittest.TestCase):
    def setUp(self):
        for cls in CLASSES:
            cls.id = 1  # ids are class-level counters

    def test_ids_auto_increment(self):
        for cls, args in [(Customer, ("a", "b", "c")), (Equipment, ("e",)), (Trainer, ("t",)),
                          (Subscription, ("d", 1, 1, 1)), (ExercisePlan, (1, 1, 20))]:
            with self.subTest(cls=cls.__name__):
                self.assertEqual([cls(*args).id, cls(*args).id], [1, 2])
                self.assertEqual(cls.get_next_id(), 3)

    def test_from_hours(self):
        self.assertEqual(ExercisePlan.from_hours(1, 1, 2).duration, 120)

    def test_add_ignores_duplicates(self):
        gym = Gym()
        customer = Customer("John", "Maple Street", "john@gmail.com")
        gym.add_customer(customer)
        gym.add_customer(customer)
        self.assertEqual(gym.customers, [customer])

    def test_subscription_info_uses_subscribed_plan(self):
        gym = Gym()
        gym.add_customer(Customer("John", "Maple Street", "john.smith@gmail.com"))
        gym.add_trainer(Trainer("Peter"))
        gym.add_equipment(Equipment("Treadmill"))
        gym.add_equipment(Equipment("Bike"))
        gym.add_plan(ExercisePlan(1, 1, 20))
        gym.add_plan(ExercisePlan(1, 2, 45))
        gym.add_subscription(Subscription("14.05.2020", 1, 1, 2))
        self.assertEqual(gym.subscription_info(1),
                         "Subscription <1> on 14.05.2020\n"
                         "Customer <1> John; Address: Maple Street; Email: john.smith@gmail.com\n"
                         "Trainer <1> Peter\n"
                         "Equipment <2> Bike\n"
                         "Plan <2> with duration 45 minutes")


if __name__ == "__main__":
    unittest.main()
