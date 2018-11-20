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

def check_existing_accounts(app_account):
    '''
    Function that check if a account exists with that account name and return a Boolean
    '''
    return Account.account_exist(app_account)

def display_accounts():
    '''
    Function that returns all the saved account
    '''
    return Account.display_accounts()


def main():
    print("WELCOME TO BETTYS' APP SIGN UP TO CONTINUE")

    print("What is your name?")
    app_account = input()

    print("Enter new password")
    password = input()

    print("YAAAS !!!  BETTY JUST SIGNED YOU UP")

    print(f"Hello {app_account}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new Account, dc - display contacts, fc -find a contact, ex -exit the contact list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print ("ENTER SITE ....")
            site = input()

            print(f"ENTER PASS FOR {site}  ...")
            l_name = input()

            save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
            print ('\n')
            print(f"New Contact {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_contact.phone_number}")
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break

    else:
        print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()