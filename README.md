# Top 10 Restaurant Scraper

This Python script prompts the user to enter the name of a city, retrieves the top 10 restaurants in that city based on food ratings and reviews via a Google search, and saves the data in a JSON file for easy reference.

---

## Features

✅ Prompts user for a **city name**  
✅ Scrapes **top 10 restaurants, ratings, and reviews**  
✅ Saves results in **`restaurants.json`**  
✅ Well-commented and clean structure for learning and clarity

---

## Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

You can install the required libraries using:

```bash
pip install requests beautifulsoup4
```

---

## How to Run

1️⃣ Clone the repository:
```bash
git clone https://github.com/naziyabanuk/top-10-restaurant-scraper.git
cd top-10-restaurant-scraper
```

2️⃣ Run the script:
```bash
python top_restaurants.py
```

3️⃣ Enter the **city name** when prompted (e.g., `Bangalore`, `Delhi`).

4️⃣ After execution, check the generated `restaurants.json` file in your folder for the scraped data.

---

## Example Output (`restaurants.json`)

```json
{
    "Restaurant Name 1": {
        "Rating": "4.5 star",
        "Reviews": "1,250 reviews"
    },
    "Restaurant Name 2": {
        "Rating": "4.4 star",
        "Reviews": "980 reviews"
    }
}
```

---

## Approach

- Uses **requests** to send HTTP requests to Google Search with the query: `top 10 restaurants in <city>`.
- Parses the returned HTML using **BeautifulSoup** to extract restaurant names, ratings, and reviews.
- Stores the top 10 restaurant details in a JSON file with restaurant names as keys for organized storage.

---

## Challenges

- Google Search frequently changes its structure; scraping may break and require adjustments.
- Handling dynamic CAPTCHA and rate limits on repeated requests is not handled here.
- For production or stable use, consider using the **Google Custom Search API, Yelp API, or Zomato API** for structured restaurant data retrieval.

---

## Contact

For any clarifications, please reach out:
- **Naziya Banu K**
- naziyabanu2001.k@gmail.com
- linkedin.com/in/Naziya-Banu-K
