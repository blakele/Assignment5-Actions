import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = 3.14
        self.assertEqual(expected, task.area(1))

    def test4(self):
        listA = [1, 2, 3, 4]
        self.assertEqual((1, 4), task.firstLastList(listA))

    def test5(self):
        dateA = "11/12/2019"
        dateB = "12/24/2019"
        expected = 12
        self.assertEqual(expected, task.date(dateA, dateB))


if __name__ == '__main__':
    unittest.main()
