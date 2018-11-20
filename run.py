#!/usr/bin/env python3.6
from account import Account 

def create_account(app_account,password):
    '''
    Function to create a new account
    '''
    new_account = Account(app_account,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()


def find_account(app_account):
    '''
    Function that finds a account by app_account name and returns the account
    '''
    return Account.find_by_app_account(app_account)

def check_existing_account(app_account):
    '''
    Function that check if a account exists with that account name and return a Boolean
    '''
    return Account.account_exist(app_account)