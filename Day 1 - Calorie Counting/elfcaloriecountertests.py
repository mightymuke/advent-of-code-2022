import unittest
from elfcaloriecounter import ElfCalorieCounter

class CalorieCounterTests(unittest.TestCase):

    def test_highest_amount_of_calories_from_example(self):
        elfdata = [
            '1',
            '2',
            '3',
            '',
            '4',
            '5'
        ]

        cc = ElfCalorieCounter()
        cc.load(elfdata)
        self.assertEqual(cc.topCalories(1)[0], 9)

    def test_highest_amount_of_calories_from_exercise_data(self):
        f = open("elf-calories.txt", "r")
        elfdata = f.readlines()
        f.close()

        cc = ElfCalorieCounter()
        cc.load(elfdata)
        self.assertEqual(cc.topCalories(1)[0], 74198)

    def test_top_three_calories_from_example(self):
        elfdata = [
            '1',
            '2',
            '3',
            '',
            '4',
            '5'
        ]

        cc = ElfCalorieCounter()
        cc.load(elfdata)
        self.assertEqual(cc.topCalories(3), [9, 6])

    def test_top_three_calories_from_exercise_data(self):
        f = open("elf-calories.txt", "r")
        elfdata = f.readlines()
        f.close()

        cc = ElfCalorieCounter()
        cc.load(elfdata)
        self.assertEqual(cc.topCalories(3), [74198, 67958, 67758])

if __name__ == '__main__':
    unittest.main()