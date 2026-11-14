import contextlib
import io
import runpy
import unittest
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    Vet = runpy.run_path(str(Path(__file__).with_name("001_vet.py")))["Vet"]


class TestVet(unittest.TestCase):
    def setUp(self):
        Vet.animals = []  # clinic-wide state is shared on the class

    def test_register_shares_clinic_space(self):
        peter, george = Vet("Peter"), Vet("George")
        for name in ["A", "B", "C"]:
            peter.register_animal(name)
        self.assertEqual(george.register_animal("D"), "D registered in the clinic")
        self.assertEqual(george.register_animal("E"), "E registered in the clinic")
        self.assertEqual(peter.register_animal("F"), "Not enough space")

    def test_unregister(self):
        peter = Vet("Peter")
        peter.register_animal("Tom")
        self.assertEqual(peter.unregister_animal("Molly"), "Molly not in the clinic")
        self.assertEqual(peter.unregister_animal("Tom"), "Tom unregistered successfully")

    def test_info(self):
        peter = Vet("Peter")
        peter.register_animal("Tom")
        self.assertEqual(peter.info(), "Peter has 1 animals. 4 space left in clinic")


if __name__ == "__main__":
    unittest.main()
