"""
The solution was to separate User responsibilities into separate classes: EmailSender and DatabaseSaver.
"""


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email


class EmailSender:
    def send_email(self, user, message):
        # Code to send email
        pass


class DatabaseSaver:
    def save_to_database(self, user):
        # Code to save user to database
        pass
