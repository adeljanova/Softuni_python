from project.movie import Movie
from unittest import TestCase


class MovieTests(TestCase):
    NAME = "Alice in Wonderland"
    YEAR = 1989
    RATING = 7
    MIN_YEAR = 1951

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_init(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_empty_setter_if_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_year_empty_setter_if_raises_error(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = self.MIN_YEAR - 10

        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_name_append_name_when_does_not_exist(self):
        first_name = "Pesho"
        second_name = "Gosho"

        self.movie.add_actor(first_name)
        self.movie.add_actor(second_name)
        self.assertEqual([first_name, second_name], self.movie.actors)

    def test_add_name_append_name_when_duplicated_names(self):
        name = "Pesho"
        self.movie.actors = [name]

        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test_gt_if_returns_true_when_first_movie_has_greater_rating(self):
        other_movie_name = "The Notebook"
        other_movie = Movie(other_movie_name, 1972, self.RATING - 4)

        first_result = self.movie > other_movie
        second_result = other_movie > self.movie

        expected_result = f'"{self.movie.name}" is better than "{other_movie_name}"'
        self.assertEqual(expected_result, first_result)
        self.assertEqual(expected_result, second_result)

    def test_repr_if_returns_proper_string(self):
        actors_list = ["Pesho", "Gosho"]
        self.movie.actors = actors_list

        actual_result = repr(self.movie)
        expected_output = f"Name: {self.NAME}\n" \
                          f"Year of Release: {self.YEAR}\n" \
                          f"Rating: {self.RATING:.2f}\n" \
                          f"Cast: {', '.join(actors_list)}"

        self.assertEqual(expected_output, actual_result)

