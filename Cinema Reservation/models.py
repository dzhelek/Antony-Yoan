class UserModel:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        # TODO: Implement a validation -> Raise an error
        pass

    def __str__(self):
        return f'{self.id} | {self.username} | {self.email} | {self.password}'
