import unittest
from user_registration import valid_first_name,valid_last_name,valid_email_id,mob_num_valid,valid_password,valid_password

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
        self.assertEqual(valid_email_id("abc@yahoo.com"), 1)
        self.assertEqual(valid_email_id("abc-100@yahoo.com"), 1)
        self.assertEqual(valid_email_id("abc.100@yahoo.com"), 1)
        self.assertEqual(valid_email_id("abc111@abc.com"), 1)
        self.assertEqual(valid_email_id("abc111@abc.net"), 1)
        self.assertEqual(valid_email_id("abc.100@abc.com.au"), 1)
        self.assertEqual(valid_email_id("abc@1.com"), 1)
        self.assertEqual(valid_email_id("abc@gmail.com.com"), 1)
        self.assertEqual(valid_email_id("abc+100@gmail.com"), 1)
        self.assertEqual(valid_email_id("abc@.com.my"), 1)
        self.assertEqual(valid_email_id("abc123@.com.com"), 1)
        self.assertEqual(valid_email_id(".abc@abc.com"), 1)
        self.assertEqual(valid_email_id("abc..2002@gmail.com"), 1)
        self.assertEqual(valid_email_id("abc.@gmail.com"), 1)
        self.assertEqual(valid_email_id("abc@gmail.com.aa.au"), 1) 

        self.assertEqual(valid_email_id("abc"), 0)
        self.assertEqual(valid_email_id("abc123@gmail.a"), 0)
        self.assertEqual(valid_email_id("abc123@.com"), 0)
        self.assertEqual(valid_email_id("abc()*@gmail.com"), 0)
        self.assertEqual(valid_email_id("abc@%*.com"), 0)
        self.assertEqual(valid_email_id("abc@abc@gmail.com"), 0)
        self.assertEqual(valid_email_id("abc@gmail.com.1a"), 0)
              

    def test_check_mobile_numb_valid(self):
        self.assertEqual(mob_num_valid('91 8217439063'),1)
        self.assertEqual(mob_num_valid("+91 8217439063"),1) 
        self.assertEqual(mob_num_valid("*91 8217439063"),0) 
        self.assertEqual(mob_num_valid("918217439063"),0) 

    def test_check_password_valid(self):
    
        self.assertEqual(valid_password('@Bridgelabs2Future'),1)
        self.assertEqual(valid_password("BridgelabsFuture"),0)

        

if __name__ == '__main__':
    unittest.main()