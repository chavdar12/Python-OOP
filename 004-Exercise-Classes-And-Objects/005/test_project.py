import unittest

from project.section import Section
from project.task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.task = Task("Make bed", "27/05/2020")

    def test_change_name(self):
        self.assertEqual(self.task.change_name("Make bed"), "Name cannot be the same.")
        self.assertEqual(self.task.change_name("Go to University"), "Go to University")

    def test_change_due_date(self):
        self.assertEqual(self.task.change_due_date("27/05/2020"), "Date cannot be the same.")
        self.assertEqual(self.task.change_due_date("28.05.2020"), "28.05.2020")

    def test_comments(self):
        self.task.add_comment("Don't forget laptop")
        self.assertEqual(self.task.edit_comment(0, "Laptop and notebook"), "Laptop and notebook")
        self.assertEqual(self.task.edit_comment(1, "x"), "Cannot find comment.")
        self.assertEqual(self.task.edit_comment(-1, "x"), "Cannot find comment.")

    def test_details(self):
        self.assertEqual(self.task.details(), "Name: Make bed - Due Date: 27/05/2020")


class TestSection(unittest.TestCase):
    def setUp(self):
        self.section = Section("Daily tasks")
        self.task = Task("Make bed", "27/05/2020")

    def test_add_task(self):
        self.assertEqual(self.section.add_task(self.task),
                         "Task Name: Make bed - Due Date: 27/05/2020 is added to the section")
        self.assertEqual(self.section.add_task(Task("Make bed", "01/01/2021")),
                         "Task is already in the section Daily tasks")

    def test_complete_task(self):
        self.section.add_task(self.task)
        self.assertEqual(self.section.complete_task("Make bed"), "Completed task Make bed")
        self.assertTrue(self.task.completed)
        self.assertEqual(self.section.complete_task("Nope"), "Could not find task with the name Nope")

    def test_clean_section_removes_consecutive_completed(self):
        for name in ["a", "b", "c"]:
            self.section.add_task(Task(name, "d"))
            self.section.complete_task(name)
        self.section.add_task(Task("keep", "d"))
        self.assertEqual(self.section.clean_section(), "Cleared 3 tasks.")
        self.assertEqual([t.name for t in self.section.tasks], ["keep"])

    def test_view_section(self):
        self.section.add_task(self.task)
        self.assertEqual(self.section.view_section(), "Section Daily tasks:\nName: Make bed - Due Date: 27/05/2020")


if __name__ == "__main__":
    unittest.main()
