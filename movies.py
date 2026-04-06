import movie_storage
import statistics
import random


def main():
    """
    Main entry point for the Movie CLI application.

    Handles the main menu, user input, and calls appropriate
    functions for listing, adding, deleting, updating movies,
    showing stats, picking a random movie, searching, and sorting.
    """
    print("Welcome to the Movie Database!")
    while True:
        print_menu()
        choice = input("Enter choice (1-8, 0 to Exit): ").strip()

        # Changed: Exit moved to the bottom of the menu
        if choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            stats()
        elif choice == "6":
            random_movie()
        elif choice == "7":
            search_movie()
        elif choice == "8":
            sort_movies()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 8.\n")


def print_menu():
    """Prints the main menu for the movie application."""
    print("*" * 10, "My Movie Database", "*" * 10)
    print()
    print("Menu:")
    print("1. List Movies")
    print("2. Add Movie")
    print("3. Delete Movie")
    print("4. Update Movie")
    print("5. Stats")
    print("6. Random Movie")
    print("7. Search Movie")
    print("8. Movies Sorted by Rating")
    print("0. Exit")  # Exit at the bottom, Changed


def list_movies():
    """
    Lists all movies in the database with their year and rating.

    Loads movies from the JSON file using movie_storage.
    """
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database.")
        return

    print(f"{len(movies)} movies total:")
    for title, info in movies.items():
        print(f"{title} ({info['year']}) - Rating: {info['rating']}")


def add_movie():
    """
    Adds a new movie to the database.

    Parameters:
        None

    Returns:
        None

    Prompts the user for title, year, and rating.
    Uses movie_storage.add_movie to persist data.
    """
    movies = movie_storage.get_movies()

    while True:
        title = input("Enter movie title: ").strip()
        if not title:
            print("Title cannot be empty. Try again.")
        elif title in movies:
            print(f"Movie '{title}' already exists!")
        else:
            break

    while True:
        year_input = input("Enter year of release: ").strip()
        if not year_input.isdigit():
            print("Year must be a number. Try again.")
        else:
            year = int(year_input)
            break

    while True:
        rating_input = input("Enter movie rating (1-10): ").strip()
        try:
            rating = float(rating_input)
            if rating < 1 or rating > 10:
                print("Rating must be between 1 and 10. Try again.")
            else:
                break
        except ValueError:
            print("Rating must be a number. Try again.")

    movie_storage.add_movie(title, year, rating)
    print(f"Movie '{title}' successfully added.")


def delete_movie():
    """
    Deletes a movie from the database.

    Prompts the user for the movie title.
    Uses movie_storage.delete_movie to persist data.

    Parameters:
        None

    Returns:
        None
    """
    movies = movie_storage.get_movies()
    title = input("Enter movie title to delete: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    if title not in movies:
        print("Movie not found.")
        return
    movie_storage.delete_movie(title)
    print(f"Movie '{title}' deleted.")


def update_movie():
    """
    Updates the rating of an existing movie.

    Prompts the user for title and new rating.
    Uses movie_storage.update_movie to persist data.

    Parameters:
        None

    Returns:
        None
    """
    movies = movie_storage.get_movies()
    title = input("Enter movie title to update: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    if title not in movies:
        print("Movie not found.")
        return

    while True:
        rating_input = input("Enter new rating (1-10): ").strip()
        try:
            rating = float(rating_input)
            if rating < 1 or rating > 10:
                print("Rating must be between 1 and 10. Try again.")
            else:
                break
        except ValueError:
            print("Rating must be a number. Try again.")

    movie_storage.update_movie(title, rating)
    print(f"Movie '{title}' updated.")


def stats():
    """
    Displays statistics about the movies database:
    - Average rating
    - Median rating
    - Best and worst rated movies

    Parameters:
        None

    Returns:
        None
    """
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database.")
        return

    ratings = [info['rating'] for info in movies.values()]
    avg = sum(ratings) / len(ratings)
    med = statistics.median(ratings)
    max_rating = max(ratings)
    min_rating = min(ratings)

    best = [title for title, info in movies.items() if info['rating'] == max_rating]
    worst = [title for title, info in movies.items() if info['rating'] == min_rating]

    print(f"Average rating: {avg:.2f}")
    print(f"Median rating: {med}")
    print("Best movie(s):", ", ".join(best))
    print("Worst movie(s):", ", ".join(worst))


def random_movie():
    """Displays a random movie from the database."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database.")
        return
    title = random.choice(list(movies.keys()))
    info = movies[title]
    print(f"{title} ({info['year']}) - Rating: {info['rating']}")


def search_movie():
    """Searches for movies containing a substring in the title."""
    movies = movie_storage.get_movies()
    query = input("Enter part of the movie name: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    found = False
    for title, info in movies.items():
        if query in title.lower():
            print(f"{title} ({info['year']}) - Rating: {info['rating']}")
            found = True
    if not found:
        print("No matching movies found.")


def sort_movies():
    """Displays all movies sorted by rating (descending)."""
    movies = movie_storage.get_movies()
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]['rating'], reverse=True)
    for title, info in sorted_movies:
        print(f"{title} ({info['year']}) - Rating: {info['rating']}")


if __name__ == "__main__":
    main()
