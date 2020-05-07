from views import UserViews
from controllers import UserController
from models import UserModel


class UserViewControllerManager:
    def __init__(self):
        self.views = UserViews()
        self.controllers = UserController()

    def manage_entering_system_views_and_controllers(self):
        is_system_entered = False
        user_entered_system = None
        while not is_system_entered:
            command = self.views.console_read_command_view()
            if command == 'help':
                self.views.guest_user_help_view()
            elif command == 'login':
                user_entered_system = self.manage_login_view_and_controller()
            elif command == 'signup':
                user_entered_system = self.manage_signup_view_and_controller()
            elif command == 'exit':
                user_entered_system = self.manage_exit_view_and_controller()
            else:
                print(f'\'{command}\' command not found')
            if user_entered_system is not None:
                is_system_entered = True

        return user_entered_system

    def manage_login_view_and_controller(self):
        login_data = self.views.login()
        username_entered = login_data[0]
        password_entered = login_data[1]
        try:
            return self.controllers.log_user(username_entered, password_entered)
        except ValueError as err:
            self.views.error_view(str(err))

    def manage_user_commands_views_and_controllers(self, user):
        self.views.welcome_user(user)

    def manage_signup_view_and_controller(self):
        signup_data = self.views.signup()
        username_entered = signup_data[0]
        email_entered = signup_data[1]
        password_entered = signup_data[2]
        try:
            self.controllers.sign_user(username_entered, email_entered, password_entered)
            return self.controllers.select_user_by_username(username_entered, password_entered)
        except Exception as err:
            error_message_fields = str(err).split('.')
            message_to_print = f'User with this {error_message_fields[1]} already exists!'
            self.views.error_view(message_to_print)

    def manage_exit_view_and_controller(self):
        return self.views.exit()

    def release_resources(self):
        self.controllers.gateway.db.close()