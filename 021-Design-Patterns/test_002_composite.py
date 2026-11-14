import runpy
import unittest
from pathlib import Path

ns = runpy.run_path(str(Path(__file__).with_name("002_composite.py")))
Folder, File = ns["Folder"], ns["File"]


class TestComposite(unittest.TestCase):
    def setUp(self):
        self.root = Folder("root")
        self.docs = Folder("docs")
        self.root.add_child(self.docs)
        self.file = File("a.txt")
        self.docs.add_child(self.file)

    def test_get_path(self):
        self.assertEqual(self.file.get_path(), "root/docs/a.txt")
        self.assertEqual(self.root.get_path(), "root")

    def test_move(self):
        self.file.move(self.root)
        self.assertEqual(self.file.get_path(), "root/a.txt")
        self.assertNotIn(self.file, self.docs.children)

    def test_delete(self):
        self.file.delete()
        self.assertEqual(self.docs.children, [])
        self.assertIsNone(self.file.parent)


if __name__ == "__main__":
    unittest.main()
