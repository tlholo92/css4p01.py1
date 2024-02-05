
import pandas as pd
from collections import Counter

# Load the dataset
file_path = 'movie_dataset.csv'
movies_df = pd.read_csv(file_path)

# Data Cleaning
# Rename columns to remove spaces and standardize names
movies_df.columns = movies_df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
# Handle missing values by filling with median for 'Revenue_Millions' and 'Metascore'
movies_df['Revenue_Millions'].fillna(movies_df['Revenue_Millions'].median(), inplace=True)
movies_df['Metascore'].fillna(movies_df['Metascore'].median(), inplace=True)

# Analysis
# Highest rated movie
highest_rated_movie = movies_df.loc[movies_df['Rating'].idxmax()]['Title']

# Average revenue of all movies
average_revenue_all_movies = movies_df['Revenue_Millions'].mean()

# Average revenue of movies from 2015 to 2017
average_revenue_2015_to_2017 = movies_df[(movies_df['Year'] >= 2015) & (movies_df['Year'] <= 2017)]['Revenue_Millions'].mean()

# Number of movies released in 2016
movies_released_in_2016 = movies_df[movies_df['Year'] == 2016].shape[0]

# Movies directed by Christopher Nolan
movies_directed_by_christopher_nolan = movies_df[movies_df['Director'] == 'Christopher Nolan'].shape[0]

# Movies with a rating of at least 8.0
movies_with_rating_at_least_8 = movies_df[movies_df['Rating'] >= 8.0].shape[0]

# Median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = movies_df[movies_df['Director'] == 'Christopher Nolan']['Rating'].median()

# Year with the highest average rating
year_with_highest_avg_rating = movies_df.groupby('Year')['Rating'].mean().idxmax()

# Percentage increase in the number of movies made between 2006 and 2016
movies_in_2006 = movies_df[movies_df['Year'] == 2006].shape[0]
movies_in_2016 = movies_df[movies_df['Year'] == 2016].shape[0]
percentage_increase_2006_to_2016 = ((movies_in_2016 - movies_in_2006) / movies_in_2006) * 100

# Most common actor
all_actors = movies_df['Actors'].str.split(',').sum()
most_common_actor = Counter(all_actors).most_common(1)[0][0].strip()

# Number of unique genres
all_genres = movies_df['Genre'].str.split(',').sum()
unique_genres = len(set(all_genres))

# Correlation of numerical features
correlation_matrix = movies_df[['Runtime_Minutes', 'Year', 'Rating', 'Votes', 'Revenue_Millions', 'Metascore']].corr()

# Print results (optional)
print(f"Highest rated movie: {highest_rated_movie}")
print(f"Average revenue of all movies: {average_revenue_all_movies}")
print(f"Average revenue of movies from 2015 to 2017: {average_revenue_2015_to_2017}")
print(f"Number of movies released in 2016: {movies_released_in_2016}")
print(f"Movies directed by Christopher Nolan: {movies_directed_by_christopher_nolan}")
print(f"Movies with a rating of at least 8.0: {movies_with_rating_at_least_8}")
print(f"Median rating of movies directed by Christopher Nolan: {median_rating_nolan_movies}")
print(f"Year with the highest average rating: {year_with_highest_avg_rating}")
print(f"Percentage increase in movies from 2006 to 2016: {percentage_increase_2006_to_2016}%")
print(f"Most common actor: {most_common_actor}")
print(f"Number of unique genres: {unique_genres}")
print("Correlation Matrix:")
print(correlation_matrix)
