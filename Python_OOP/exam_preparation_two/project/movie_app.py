from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_by_username = {}

    def register_user(self, username: str, age: int):
        user = self.__get_user_by_username(username)
        if user not in self.users_collection:
            self.users_collection.append(user)
            self.users_by_username[username] = age
            return f"{username} registered successfully."
        raise Exception("User already exists!")

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)
        if user not in self.users_collection:
            raise Exception("This user does not exist!")
        if user in self.users_collection and movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if user in self.users_collection and movie in user.movies_owned:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user_by_username(username)
        if movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        movie = Movie(**kwargs)
        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)
        if movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{user.username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)
        if movie in user.movies_owned:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{user.username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{user.username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{user.username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{user.username} disliked {movie.title} movie."

    def display_movies(self):
        movies_displayed = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))
        if not movies_displayed:
            return "No movies found."
        return '\n'.join([m.details() for m in movies_displayed])

    def __str__(self):
        result = "All users: "
        if self.users_collection:
            result += f"{', '.join(self.users_collection)}"
        else:
            result += "No users."

        result += '\n' + "All movies: "
        if self.movies_collection:
            result += f"{', '.join(self.movies_collection)}"
        else:
            result += "No movies."

        return result

    def __get_user_by_username(self, username):
        return self.users_by_username.get(username, None)
