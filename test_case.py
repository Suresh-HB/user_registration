import unittest
from user_registration import valid_first_name

class TestCheckName(unittest.TestCase):

    def test_check_name_valid(self):
        self.assertEqual(valid_first_name('Jagadeesh'), 1)
        self.assertEqual(valid_first_name('Suresh'), 1)
        self.assertEqual(valid_first_name('Jo'), 0)
        self.assertEqual(valid_first_name('tarun'), 0)
        self.assertEqual(valid_first_name('al'), 0)
        self.assertEqual(valid_first_name('aLice'), 0)

if __name__ == '__main__':
    unittest.main()
