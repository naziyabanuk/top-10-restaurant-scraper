# Top 10 Restaurant Scraper

This Python script automatically scrapes the **top 10 restaurants in a specified city** from Google Search using **Selenium with ChromeDriver**.

It extracts:
✅ **Restaurant Names**  
✅ **Ratings**  
✅ **Reviews Count**

and stores them in a clean **JSON file (`restaurants.json`)** for analysis, reporting, or automation use.

---

## 🚀 Features

- **Prompts the user** to enter the city name.
- **Searches Google** for “top 10 restaurants in <city>”.
- Clicks **“More places”** to expand the list.
- **Scrapes names, ratings, and reviews dynamically**.
- Outputs the data into a structured JSON file.
- Uses **Selenium with WebDriver Manager** for smooth, automatic ChromeDriver handling.

---

## 🛠️ Requirements

- Python 3.x
- Google Chrome installed
- Packages:
    - selenium
    - webdriver-manager

---

## ⚙️ Installation

1️⃣ Clone the repository or download the script:
```bash
git clone https://github.com/naziyabanuk/top-10-restaurant-scraper.git
cd top-10-restaurant-scraper
```

2️⃣ Install dependencies:
```bash
pip install selenium webdriver-manager
```

---

## ▶️ Usage

Run the script:
```bash
python top_restaurants_scraper.py
```

Enter the **name of the city** when prompted, e.g.:
```
Enter the name of the city: Bangalore
```

After successful execution, the script will generate:
```
restaurants.json
```
containing the top 10 restaurants with their ratings and reviews.

---

Sample Output (`restaurants.json`)
```json
{
    "Restaurant Name 1": {
        "Rating": "Rated 4.4 out of 5",
        "Reviews": "2.4K"
    },
    "Restaurant Name 2": {
        "Rating": "Rated 4.2 out of 5",
        "Reviews": "876"
    }
}
```

---


Challenges Faced
    Google frequently changes its DOM structure, so XPath may need updates over time.
    Google may show “Are you a robot?” (reCAPTCHA) when automating search scraping.
    A manual delay is added in the script (time.sleep) to give you time to verify the CAPTCHA manually before scraping proceeds.

    For stable, production-grade scraping, using official APIs (Google Places API, Yelp API) is recommended.

---

## 📧 Contact

For any queries, please contact:

Naziya Banu K 
Email: [naziyabanu2001.k@gmail.com]  
GitHub: [github.com/naziyabanuk](https://github.com/naziyabanuk)
