import runpy
import unittest
from pathlib import Path

ns = runpy.run_path(str(Path(__file__).with_name("001_abstract_factory.py")))


class TestAbstractFactory(unittest.TestCase):
    def test_each_factory_creates_its_style(self):
        for name, style in [("VictorianFactory", "Victorian"), ("ModernFactory", "Modern"), ("FuturisticFactory", "Futuristic")]:
            factory = ns[name]()
            self.assertIsInstance(factory, ns["AbstractFactory"])
            self.assertEqual(str(factory.create_chair()), f"{style} chair")
            self.assertIsInstance(factory.create_sofa(), ns["Sofa"])
            self.assertIsInstance(factory.create_table(), ns["Table"])

    def test_abstract_factory_cannot_be_created(self):
        with self.assertRaises(TypeError):
            ns["AbstractFactory"]()


if __name__ == "__main__":
    unittest.main()
