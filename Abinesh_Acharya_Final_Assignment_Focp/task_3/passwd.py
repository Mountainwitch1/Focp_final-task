# passwd.py
from password_util import encrypt_password, check_password
import getpass

def change_password(username, current_password, new_password, passwd_file):
    with open(passwd_file, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith(f'{username}:'):
            parts = line.strip().split(':')
            if len(parts) == 3:
                _, _, current_encrypted_password = parts
                if check_password(current_encrypted_password, current_password):
                    lines[i] = f'{username}:{parts[1]}:{encrypt_password(new_password)}\n'
                    with open(passwd_file, 'w') as file:
                        file.writelines(lines)
                    print('Password changed.')
                    return
                else:
                    print('Current password is invalid.')
                    return
            else:
                print('Invalid entry in password file.')
                return
    
    print('User not found.')

if __name__ == "__main__":
    passwd_file = 'passwd.txt'
    username = input('User: ')
    current_password = getpass.getpass('Current Password: ')
    new_password = getpass.getpass('New Password: ')
    confirm_password = getpass.getpass('Confirm: ')

    if new_password == confirm_password:
        change_password(username, current_password, new_password, passwd_file)
    else:
        print('Passwords do not match.')

