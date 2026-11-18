import unittest

from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.title, "Wrong title")
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_empty_task_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task = self.manager.add_task("Read chapter 3")
        self.manager.complete_task(task.id)
        self.assertTrue(task.completed)

    def test_delete_task(self):
        task = self.manager.add_task("Submit report")
        self.manager.delete_task(task.id)
        self.assertEqual(len(self.manager.list_tasks()), 0)

    def test_delete_invalid_id_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)


if __name__ == "__main__":
    unittest.main()
