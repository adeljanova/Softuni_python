import sys

num_movies = int(input())
best_movie = ''
worst_movie = ''
top_rating = -sys.maxsize
worst_rating = sys.maxsize
average = 0

for i in range(1, num_movies + 1):
    movie_name = input()
    rating = float(input())
    average += rating

    if rating > top_rating:
        top_rating = rating
        best_movie = movie_name
    if rating < worst_rating:
        worst_rating = rating
        worst_movie = movie_name
average /= num_movies
print(f"{best_movie} is with highest rating: {top_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {worst_rating:.1f}")
print(f"Average rating: {average:.1f}")

