import unittest #The unittest module imported
from account import Account #Imported our account class
from account import Site #Imported the sites class !!
import pyperclip
 

class TestAccount(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Betty","goodvibez")

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
            test_account = Account("","") 
            test_account.save_account()

            self.new_account.delete_account()
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

    def test_display_all_account(self):
        '''
        method that returns a list of all account saved
        '''

        self.assertEqual(Account.display_account(),Account.account_list)


    '''def test_copy_app_account(self):

        self.new_account.save_account()
        Account.copy_app_account("Betty")

        self.assertEqual(self.new_account.app_account,pyperclip.paste())
    '''

class TestSite(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Site("facebook","wakanda") 
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.site,"facebook")
        self.assertEqual(self.new_account.sitepass,"wakanda")

    def test_save_site(self):
       
        self.new_account.save_site() 
        self.assertEqual(len(Site.site_list),1)


    def test_save_multiple_site(self):
                 
        self.new_account.save_site()
        test_account = Site("","")
        test_account.save_site()
        self.assertEqual(len(Site.site_list),2)
                

if __name__ == '__main__':
    unittest.main()
