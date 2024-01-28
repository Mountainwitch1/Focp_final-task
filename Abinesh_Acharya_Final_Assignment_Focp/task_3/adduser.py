# adduser.py
from password_util import encrypt_password

def add_user(username, real_name, password, passwd_file):
    with open(passwd_file, 'a') as file:
        encrypted_password = encrypt_password(password)
        file.write(f'{username}:{real_name}:{encrypted_password}\n')
    print('User Created.')

if __name__ == "__main__":
    passwd_file = 'passwd.txt'
    username = input('Enter new username: ')
    real_name = input('Enter real name: ')
    password = input('Enter password: ')
    
    with open(passwd_file, 'r') as file:
        existing_users = [line.split(':')[0] for line in file]

    if username in existing_users:
        print('Cannot add. Most likely username already exists.')
    else:
        add_user(username, real_name, password, passwd_file)
