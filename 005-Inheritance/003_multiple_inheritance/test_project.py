import unittest

from project.teacher import Teacher


class TestTeacher(unittest.TestCase):
    def test_multiple_inheritance(self):
        teacher = Teacher()
        self.assertEqual(teacher.teach(), "teaching...")
        self.assertEqual(teacher.sleep(), "sleeping...")
        self.assertEqual(teacher.get_fired(), "fired...")


if __name__ == "__main__":
    unittest.main()
