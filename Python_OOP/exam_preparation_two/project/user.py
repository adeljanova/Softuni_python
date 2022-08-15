class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value or value is not str:
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value is not int or value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}"

        if self.movies_liked:
            movies_liked = '\n'.join([m.details() for m in self.movies_liked])
            result += '\n' + "Liked movies:" + f"{movies_liked}"
        else:
            result += '\n' + "No movies liked."

        if self.movies_owned:
            movies_owned = '\n'.join([m.details() for m in self.movies_owned])
            result += '\n' + "Owned movies:" + f"{movies_owned}"
        else:
            result += '\n' + "No movies owned."

        return result.strip()

