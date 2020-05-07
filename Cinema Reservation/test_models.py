import unittest

from models import UserModel


class TestValidatePassword(unittest.TestCase):
    def test_password_shorter_than_eight_symbols_returns_false(self):
        password = '1234567'

        result = UserModel.validate_password(password)

        self.assertFalse(result, 'shorter than eight')

    def test_long_password_with_no_capital_letters_returns_false(self):
        password = '12345678'

        result = UserModel.validate_password(password)

        self.assertFalse(result, 'no capital letters')

    def test_long_password_with_capital_letter_without_special_symbols(self):
        password = '12345678A'

        result = UserModel.validate_password(password)

        self.assertFalse(result, 'no special symbols')

    def test_password_with_eigh_symbols_with_one_capital_and_one_special(self):
        password = 'A12$4567'

        result = UserModel.validate_password(password)

        self.assertTrue(result, 'the password is correct')


class TestValidateEmail(unittest.TestCase):
    def test_email_without_at_symbol_returns_false(self):
        email = 'example.example.com'

        result = UserModel.validate_email(email)

        self.assertFalse(result)

    def test_email_with_at_symbol_but_unvalid_returns_false(self):
        email1 = 'example@example@com'
        email2 = 'example@'
        # email3 = '@example.com'

        result1 = UserModel.validate_email(email1)
        result2 = UserModel.validate_email(email2)
        # result3 = UserModel.validate_email(email3)

        self.assertFalse(result1)
        self.assertFalse(result2)
        # self.assertFalse(result3)

    def test_with_correct_input_returns_true(self):
        email = 'name@example.com'

        result = UserModel.validate_email(email)

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
