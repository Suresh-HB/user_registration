import unittest
from user_registration import valid_first_name,valid_last_name,valid_email_id

class TestCheckName(unittest.TestCase):

    def test_check_name_valid(self):
        self.assertEqual(valid_first_name('Jagadeesh'), 1)
        self.assertEqual(valid_first_name('Suresh'), 1)
        self.assertEqual(valid_first_name('Jo'), 0)
        self.assertEqual(valid_first_name('tarun'), 0)
        self.assertEqual(valid_first_name('al'), 0)
        self.assertEqual(valid_first_name('aLice'), 0)

    def test_check_last_name_valid(self):
        self.assertEqual(valid_last_name("Hbp"),1)
        self.assertEqual(valid_last_name("hb"),0)

    def test_check_email_valid(self):
        self.assertEqual(valid_email_id("LconKact@bl.co.in"),1)
        self.assertEqual(valid_email_id("Abchfg12@oocom"),0)        


if __name__ == '__main__':
    unittest.main()