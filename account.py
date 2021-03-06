import pyperclip


class Account:
    """
    Class that generates new instances of the  Accounts.
    """

    account_list = [] # Empty account list

    def __init__(self,app_account,password):

      # docstring removed for simplicity

        self.app_account = app_account
        self.password = password

    def save_account(self):

        

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_name(cls,app_account):


        for account in cls.account_list:
            if account.app_account == app_account:
                return account

    @classmethod
    def display_account(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    @classmethod
    def copy_app_account(cls,app_account):
        account_found = Account.find_by_app_account(app_account)
        pyperclip.copy(account_found.app_account)


class Site:
    """
    Class that generates new instances of the  sites and passwords.
    """

    site_list = []

    def __init__(self,site,sitepass):

      # docstring removed for simplicity

        self.site = site
        self.sitepass = sitepass
    
    
    def tearDown(self):
           
        Site.site_list = []

    def save_site(self):

        Site.site_list.append(self)

    
    def test_save_multiple_site(self):
            
            self.new_account.save_site()
            test_account = Site("","")
            test_account.save_site()
            self.assertEqual(len(Site.site_list),2)
    