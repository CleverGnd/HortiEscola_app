import json


class Authenticator:
    def __init__(self, user_file):
        self.user_file = user_file

    def register(self, user):
        with open(self.user_file, "a") as file:
            file.write(user.to_json() + "\n")

    def authenticate(self, username, password):
        with open(self.user_file, "r") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    return True
        return False
