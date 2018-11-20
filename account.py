class Account:
    """
    Class that generates new instances of the  Accounts.
    """

    account_list = [] # Empty contact list

    def __init__(self,app_account,password):

      # docstring removed for simplicity

        self.app_account = app_account
        self.password = password

    def save_account(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    

    @classmethod
    def display_account(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list