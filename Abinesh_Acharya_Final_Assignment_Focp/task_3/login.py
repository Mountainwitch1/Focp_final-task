# login.py
from password_util import check_password
import getpass

def login(username, password, passwd_file):
    with open(passwd_file, 'r') as file:
        for line in file:
            stored_username, _, stored_encrypted_password = line.strip().split(':')
            if stored_username == username and check_password(stored_encrypted_password, password):
                print('Access granted.')
                return
    print('Access denied.')

if __name__ == "__main__":
    passwd_file = 'passwd.txt'
    username = input('User: ')
    password = getpass.getpass('Password: ')
    

    login(username, password, passwd_file)
