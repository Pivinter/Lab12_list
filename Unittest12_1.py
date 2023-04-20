import unittest
from Lab12_1 import *

class TestNotebookApp(unittest.TestCase):

    def test_days_in_month(self):
        self.assertEqual(days_in_month(2, 2020), 29)
        self.assertEqual(days_in_month(2, 2021), 28)
        self.assertEqual(days_in_month(1, 2021), 31)
        self.assertEqual(days_in_month(4, 2021), 30)

    def test_note_creation(self):
        note = Note("Петров", "Іван", "1234567890", [18, 4, 2000])
        self.assertEqual(note.surname, "Петров")
        self.assertEqual(note.name, "Іван")
        self.assertEqual(note.phone_number, "1234567890")
        self.assertEqual(note.birth_date, [18, 4, 2000])

if __name__ == "__main__":
    unittest.main()
