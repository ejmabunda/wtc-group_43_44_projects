"""This module provides the PasswordManager class
"""
from cryptography.fernet import Fernet
import json


class PasswordManager:
    """Represents a password manager, a tool that stores
    and encrypts passwords. All data is protected by a
    master mastermind and stored in a JSON file.
    
    Attributes:
        master_password(str): The password used to unlock
            the password manager
        credentials(list[str]): A list of objects that 
            represent credentials
        path(str): The path to the passwords file
    """
    def __init__(self, path: str = 'passwords.json') -> None:
        self.__key = Fernet.generate_key()
        self.f = Fernet(self.__key)

        self.__path = path
        self.__master_password = ''
        self.__credentials = []

        self.unlock()
        self.start()


    def start(self) -> None:
        """Displays the UI in the console, providing the
        following options:
        - Add a password
        - View a password
        - Exit
        """
        while True:
            choice = input('Choose an option: ')
            match choice:
                # 1 to add password
                case '1':
                    self.add_password()
                # 2 to view a password
                case '2':
                    service_name = input('Enter the service name: ')
                    credential = self.get_password(service_name)
                    if credential:
                        print(f'Username: {credential[service_name]['username']}\n')
                        print(f'Password: {credential[service_name]['password']}\n')
                    else:
                        print(f'Error: service name, {service_name} not found\n')
                # 3 to Exit
                case '3':
                    self.save()
                    break


    def unlock(self):
        """Try to unlock passwords with master password
        """
        # Load data from password file
        data = self.load(self.path)

        # Check 
        if data['master_password'] == '':
            password = input('Choose a strong password: ')
        else:
            # Try to unlock with master password
            password = input('Enter the password: ')
            while password != self.f.decrypt(self.master_password):
                password = input('Try again: ')
            print('Password Manager unlocked!')

        self.__credentials = data['credentials']


    def save(self) -> None:
        """Serialize a Password Manager object to a file
        """
        with open(self.path, 'w', encoding='utf-8') as fp:
            data = {
                'master_password': self.master_password,
                'credentials': self.credentials
            }
            return json.dump(data, fp)

    def load(self, path: str = 'passwords.json'):
        """Load a password manager object from a JSON file
        
        Arguments:
            path(str): The path to the passwords file

        Returns:
            PasswordManager: A password manager object
        """
        with open(self.path, 'r', encoding='utf-8') as fp:
            if fp.read() == '':
                return {
                    'master_password': '',
                    'credentials': []
                }
            return json.load(fp)

    def add_password(self):
        """Adds an encrypted password to the password manager
        """
        service_name = input('Enter the service name: ')
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        self.credentials(
            {
                'service_name': service_name,
                'username': username,
                'password': password
            }
        )
        print('New password added!')

    def get_credential(self, service_name):
        """Returns a credential based on service name
        
        Arguments:
            service_name(str): A string representing a service name

        Returns:
            object: A object representing a credential, None on failure
        """
        if service_name in self.credentials['service_name']:
            return self.credentials[service_name]
        return None

    @property
    def master_password(self) -> str:
        return self.__master_password
    
    @property
    def credentials(self) -> list:
        return self.__credentials
    
    @credentials.setter
    def credentials(self, new_credential: object):
        """Adds new entries to the credentials list
        
        Arguments:
            new_credentials(list): The list to be added
        """
        self.__credentials.append(new_credential)
    
    @property
    def path(self) -> str:
        return self.__path
