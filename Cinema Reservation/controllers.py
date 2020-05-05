from gateway import UserGateway
from views_constants import INVALID_CHOICE_RETURNED_VALUE, CHOICE_FOR_LOGIN_IN_CHOOSE_LOGIN_OR_SIGNUP, CHOICE_FOR_SIGNUP_IN_CHOOSE_LOGIN_OR_SIGNUP


class UserController:
    def __init__(self):
        self.gateway = UserGateway()

    def log_user(self, username, password):
        self.gateway.log(username=username, password=password)


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
        
