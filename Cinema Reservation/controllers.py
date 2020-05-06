from gateway.gateway import UserGateway
from views_constants import INVALID_CHOICE_RETURNED_VALUE, CHOICE_FOR_LOGIN_IN_CHOOSE_LOGIN_OR_SIGNUP, CHOICE_FOR_SIGNUP_IN_CHOOSE_LOGIN_OR_SIGNUP


class UserController:
    def __init__(self):
        self.gateway = UserGateway()

    def log_user(self, username, password):
        user_data = self.gateway.search_user_by_name(username=username, password=password)
        if user_data is not None:
            if password == user_data[3]:
                return 'Correct' #view for correct login
            else:
                return 'Invalid password'
        else:
            return 'No user with this username'

    def sign_user(self, username, email, password):
        self.gateway.update_table_with_user_data(username, email, password)


    # def create_user(self, email, password):
    #     user = self.users_gateway.create(email=email, password=password)

    #     # send email
    #     # sync with Slack

    #     return user

    # def enter_system(self, choice):
        # if choice == CHOICE_FOR_LOGIN_IN_CHOOSE_LOGIN_OR_SIGNUP:
            
        # elif choice == CHOICE_FOR_SIGNUP_IN_CHOOSE_LOGIN_OR_SIGNUP:
        #     pass
        # else:
        #     return INVALID_CHOICE_RETURNED_VALUE
        # return 0
        
