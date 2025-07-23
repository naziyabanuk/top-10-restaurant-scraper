# Top 10 Restaurants Scraper for a Given City

import requests            # For making HTTP requests to fetch web page data
from bs4 import BeautifulSoup  # For parsing and extracting information from HTML
import json                # For saving extracted restaurant data into a JSON file
import re                  # For using regular expressions to match patterns in text

# Defines a function that will take the city name input and return a dictionary of restaurant data.
def get_restaurants(city_name):

    # Replace spaces for URL encoding, Prepares a search query by inserting the city name.
    query = f"top 10 restaurants in {city_name}"
    
    # Create Google Search URL by replacing spaces with + for URL formatting.
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

    # Add user-agent to avoid blocking, Sets headers with a User-Agent to simulate a real browser and avoid blocking by Google.
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # Make HTTP GET request to Google Search page and checks if the request was successful (HTTP 200). If it fails, it prints an error and returns an empty dictionary.
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve data from Google Search")
        return {}
    
    # Parses the fetched HTML content using BeautifulSoup to allow easy element extraction.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initializes an empty dictionary to store restaurant names and their details.
    restaurant_data = {}
    
    # Google search results can vary, so we will look for patterns:
    # Tries to find all <div> elements that may contain restaurant information:
    # First, by checking for data-md attributes.
    # If none found, fallback to <div> with classes matching 'BNeawe' (commonly used in Google search snippets).
    results = soup.find_all('div', attrs={'data-md': re.compile(r'.*')})
    if not results:
        results = soup.find_all('div', class_=re.compile('BNeawe'))

    # Counter to track how many restaurants have been found so far.
    found = 0

    # Loop through found elements to extract data:
    for res in results:
        text = res.get_text(separator="\n")
        if text:
            lines = text.split('\n')

            # Loop through each line to look for lines containing a pattern like '4.5 star', indicating ratings.
            for i in range(len(lines)):
                line = lines[i]
                if re.search(r'\d\.\d star', line):
                    name = lines[i - 1] if i > 0 else "Restaurant"
                    rating = line

                    # Checks if the line below the rating contains 'reviews' and stores that as reviews if present.
                    reviews = ""
                    if i + 1 < len(lines) and 'reviews' in lines[i + 1].lower():
                        reviews = lines[i + 1]

                    # Adds the restaurant data to the restaurant_data dictionary using the restaurant name as the key.    
                    restaurant_data[name] = {
                        "Rating": rating,
                        "Reviews": reviews
                    }

                    # Increments the found count and stops if 10 restaurants are collected.
                    found += 1
                    if found >= 10:
                        break

            # Breaks the outer loop if 10 restaurants have already been found.        
            if found >= 10:
                break
    
    # If parsing fails, inform the user
    if not restaurant_data:
        print("No restaurant data could be parsed from the search results.")
    
    # Returns the dictionary containing restaurant data.
    return restaurant_data

def main():

    # Prompts the user to enter a city name and stores it in city_name.
    city_name = input("Enter the name of the city: ")

    # Calls the get_restaurants function to fetch restaurant data for the entered city.
    restaurant_data = get_restaurants(city_name)
    
    # If data is found: Opens (or creates) restaurants.json for writing, Dumps the data in a pretty JSON format.
    if restaurant_data:
        with open('restaurants.json', 'w', encoding='utf-8') as f:
            json.dump(restaurant_data, f, indent=4, ensure_ascii=False)
        print("Top 10 restaurant data saved to restaurants.json")
    else:
        print("No data saved.")

if __name__ == '__main__':
    main()
