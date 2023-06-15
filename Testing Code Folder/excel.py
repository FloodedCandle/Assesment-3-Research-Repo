import pandas as pd

# Create Cinema table
cinema_data = {
    'cinema_id': [1, 2],
    'name': ['Auckland', 'Wellington'],
    'address': ['123 Main St, Auckland', '456 Elm St, Wellington'],
    'phone_number': ['1234567890', '9876543210'],
    'email': ['info@aucklandcinema.com', 'info@wellingtoncinema.com']
}
cinema_df = pd.DataFrame(cinema_data)

# Create Theatre table
theatre_data = {
    'theatre_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'cinema_id': [1, 1, 1, 1, 1, 1, 2, 2, 2, 2],
    'name': ['Theater 1', 'Theater 2', 'Theater 3', 'Theater 4', 'Theater 5', 'Theater 6', 'Theater 1', 'Theater 2', 'Theater 3', 'Theater 4'],
    'seating_capacity': [200, 150, 300, 250, 350, 500, 100, 120, 180, 80],
    'sound_system': ['Dolby Digital EX', 'Sony SDDS', 'THX', 'Dolby Atmos', 'Dolby Digital EX', 'THX', 'Sony SDDS', 'Dolby Atmos', 'Dolby Digital EX', 'THX']
}
theatre_df = pd.DataFrame(theatre_data)

# Create Movie table
movie_data = {
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'title': ['Avengers: Endgame', 'The Lion King', 'Joker', 'Toy Story 4', 'Fast & Furious 9', 'Inception', 'Titanic', 'The Matrix', 'The Shawshank Redemption', 'Forrest Gump'],
    'director': ['Anthony Russo', 'Jon Favreau', 'Todd Phillips', 'Josh Cooley', 'Justin Lin', 'Christopher Nolan', 'James Cameron', 'Lana Wachowski', 'Frank Darabont', 'Robert Zemeckis'],
    'duration': ['3h 1min', '1h 58min', '2h 2min', '1h 40min', '2h 25min', '2h 28min', '3h 14min', '2h 16min', '2h 22min', '2h 22min'],
    'genre': ['Action, Adventure, Drama', 'Animation, Adventure, Drama', 'Crime, Drama, Thriller', 'Animation, Adventure, Comedy', 'Action, Adventure, Crime', 'Action, Adventure, Sci-Fi', 'Drama, Romance', 'Action, Sci-Fi', 'Drama', 'Drama, Romance'],
    'release_year': [2019, 2019, 2019, 2019, 2021, 2010, 1997, 1999, 1994, 1994],
    'imdb_link': [
        'https://www.imdb.com/title/tt4154796/',
        'https://www.imdb.com/title/tt6105098/',
        'https://www.imdb.com/title/tt7286456/',
        'https://www.imdb.com/title/tt1979376/',
        'https://www.imdb.com/title/tt5433138/',
        'https://www.imdb.com/title/tt1375666/',
        'https://www.imdb.com/title/tt0120338/',
        'https://www.imdb.com/title/tt0133093/',
        'https://www.imdb.com/title/tt0111161/',
        'https://www.imdb.com/title/tt0109830/'
    ]
}
movie_df = pd.DataFrame(movie_data)

# Create MovieScreening table

# Create MovieScreening table
screening_data = {
    'screening_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'movie_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'theatre_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'date': ['2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08', '2023-06-08'],
    'time': ['10:00', '13:00', '16:00', '19:00', '12:00', '15:00', '18:00', '11:00', '14:00', '17:00']
}
screening_df = pd.DataFrame(screening_data)

# Save the tables to an Excel file
with pd.ExcelWriter('cinema_data.xlsx') as writer:
    cinema_df.to_excel(writer, sheet_name='Cinema', index=False)
    theatre_df.to_excel(writer, sheet_name='Theatre', index=False)
    movie_df.to_excel(writer, sheet_name='Movie', index=False)
    screening_df.to_excel(writer, sheet_name='MovieScreening', index=False)
