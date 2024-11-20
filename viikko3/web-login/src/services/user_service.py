from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import string

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

        existing_user = default_user_repository.find_by_username(username)

        if existing_user:
            raise UserInputError(f"User with username {username} already exists")

        for i in username:
            if i not in string.ascii_lowercase or len(username) < 3:
                raise UserInputError("Username has to be at least 3 characters long and contain only letters from a-z")

        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")
        
        if string.digits not in password and string.punctuation not in password:
            raise UserInputError("Password has to include numbers or special characters")
        
        if password_confirmation != password:
            raise UserInputError("The password confirmation doesn't match the given password")
    

user_service = UserService()
