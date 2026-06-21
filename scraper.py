# Import required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Chrome browser setup
options = webdriver.ChromeOptions()

# Launch Chrome browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open IMDb Top 250 Movies page
driver.get("https://www.imdb.com/chart/top/")

# Wait for page to load completely
time.sleep(5)

# Find all movie links from the page
movie_links = driver.find_elements(
    By.CSS_SELECTOR,
    "a[href*='/title/']"
)

# Empty list to store movie data
movies = []

# Initial rank value
rank = 1

# Loop through movie links
for link in movie_links:

    # Get movie title text
    title = link.text.strip()

    # Ignore empty links
    if title != "" and len(title) > 1:

        # Store rank and movie title
        movies.append([
            rank,
            title
        ])

        print(rank, title)

        rank += 1

        # Stop after Top 250 movies
        if rank > 250:
            break

# Close browser
driver.quit()

# Convert data into DataFrame
df = pd.DataFrame(
    movies,
    columns=[
        "Rank",
        "Movie"
    ]
)

# Save data into CSV file
df.to_csv(
    "movie_data.csv",
    index=False
)

print("\nData Saved Successfully!")
print(df.head())