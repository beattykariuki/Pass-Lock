import unittest #The unittest module imported
from account import Account #Imported our account class


class TestAccount(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Betty","goodvibez") # create contact object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.app_account,"Betty")
        self.assertEqual(self.new_account.password,"goodvibez")
    
    
    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account_list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_account(self):

            self.new_account.save_account()
            test_account = Account("","")
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("","") # new contact
            test_account.save_account()

            self.new_account.delete_account()# Deleting a contact object
            self.assertEqual(len(Account.account_list),1)


    def test_find_account_by_name(self):
        '''
        test to check if we can find a account by name and display information
        '''

        self.new_account.save_account()
        test_account = Account("Betty","goodvibez") 
        test_account.save_account()

        found_account = Account.find_by_name("Betty")

        self.assertEqual(found_account.app_account,test_account.app_account)




if __name__ == '__main__':
    unittest.main()
