"""
The User class has multiple responsibilities, including sending emails and saving information to a database.
This violated the Single Responsibility Principle.
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def send_email(self, message):
        # Code to send email
        pass

    def save_to_database(self):
        # Code to save user to database
        pass
