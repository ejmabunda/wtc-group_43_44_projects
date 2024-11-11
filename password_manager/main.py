from cryptography.fernet import Fernet
import json


def add_credential(credentials, service_name, username, password):
    credentials[service_name] = {
        'username': username,
        'password': Fernet.encrypt(password)
    }

def save(data):
    with open('password.json', 'w') as file:
        json.dump(data, file)


def load(data):
    with open('password.json', 'r') as file:
        passwords = json.load(data, file)


def main():
    with open('passwords.json', 'r') as file:
        credentials = json.load()
    master = input('Enter the master password: ')
    while master != credentials['master_password']:
        print('Pasword incorrect, try again')
        master = input('Enter the master password: ')

    while True:
        menu = 'Hi, user welcome to password manager\nChoose an option below:\n1. Add credential\n2. View passwords\n3. Exit'
        print(menu)
        choice = input('>>> ')
        match int(choice):
            case 1:
                credential = input('Enter your service name, username and password: ')
                service_name, username, password = credential.split()
                credentials[service_name] = {
                    'username': username,
                    'password': Fernet.encrypt(password)
                }
                credential = {
                    'service_name': service_name,
                    'username': username,
                    'password': Fernet.encrypt(password)
                }
                save(credential)
            case 2:
                service_name = input('Enter the service name: ')
                print(f"Your password for {service_name} is {credentials[service_name]['password']}\n")
            case 3:
                print('Goodbye')
                return


if __name__ == '__main__':
    main()