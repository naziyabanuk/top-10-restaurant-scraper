from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

def scrape_restaurants(city):
    options = Options()
    # options.add_argument("--headless=new")  # Optional headless mode
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 20)

    try:
        search_query = f"top 10 restaurants in {city}"
        driver.get(f"https://www.google.com/search?q={search_query.replace(' ', '+')}")
        
        # Wait for More places button and click it
        more_places = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='More places']")))
        more_places.click()
        
        time.sleep(5)  # Allow results to load

        restaurant_data = {}
        count = 0

        # Fetch restaurant cards
        restaurants = driver.find_elements(By.XPATH, "//div[@role='heading' and @aria-level='3']")

        for i in range(len(restaurants)):
            try:
                name = restaurants[i].text.strip()

                # Fetch ratings
                rating = "N/A"
                rating_elements = driver.find_elements(
                    By.XPATH, "//div[@role='heading' and @aria-level='3']//following-sibling::div//span[contains(@aria-label,'Rated')]"
                )
                if i < len(rating_elements):
                    rating = rating_elements[i].get_attribute("aria-label")

                # Fetch reviews
                reviews = "N/A"
                review_elements = driver.find_elements(
                    By.XPATH, "//div[@role='heading' and @aria-level='3']//following-sibling::div//span[contains(@aria-label,'Rated')]/following-sibling::span"
                )
                if i < len(review_elements):
                    reviews = review_elements[i].text

                if name and name not in restaurant_data:
                    restaurant_data[name] = {
                        "Rating": rating,
                        "Reviews": reviews
                    }
                    count += 1

                    if count >= 10:
                        break

            except Exception as e:
                print(f"Skipping one card due to missing elements: {e}")

        if restaurant_data:
            with open("restaurants.json", "w", encoding="utf-8") as f:
                json.dump(restaurant_data, f, indent=4, ensure_ascii=False)
            print("Top 10 restaurant data saved to restaurants.json")
        else:
            print("No restaurant data could be parsed from the search results.")

    except Exception as e:
        print(f"Error during scraping: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    scrape_restaurants(city)
