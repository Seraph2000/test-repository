from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    # .get => another way of accessing a dictionary
    # you can also set a default value
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


# applies to any endpoint which requires authentication
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
