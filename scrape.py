from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import concurrent.futures

path_to_chromedriver = "CHANGE ME"
threads = 3 # Increase the thread count to speed up process
pages = 60 # Number of movie pages (~20 movies per page)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

URL = 'https://www.themoviedb.org/movie/top-rated'

class Movie:
    def __init__(self, title, genre, score, release, budget, revenue, duration):
        self.title = title
        self.genre = genre
        self.score = score
        self.release = release
        self.budget = budget
        self.revenue = revenue
        self.duration = duration

def convert_to_hours(time_str):
    time_str = time_str.strip()  # Remove leading/trailing whitespace or newline characters
    
    # If the string contains 'h' indicating hours are present
    if 'h' in time_str:
        parts = time_str.split()
        hours = int(parts[0].strip('h'))
        minutes = int(parts[1].strip('m') if 'm' in parts[1] else '0')  # Handle cases where there might be no minutes component.
    else:
        hours = 0
        minutes = int(time_str.strip('m'))

    total_hours = hours + minutes/60.0
    return round(total_hours, 2)



def scrape_page(page_num):
    page_movies = []
    try:
        driver = webdriver.Chrome(path_to_chromedriver)
        url = 'https://www.themoviedb.org/movie/top-rated?page='
        driver.get(url + str(page_num))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        mvs = soup.find_all("div", class_="card style_1")

        for mv in mvs:
            try:
                driver.get("https://www.themoviedb.org" + mv.h2.a['href'])
                mv_soup = BeautifulSoup(driver.page_source, 'html.parser')

                # Extract movie details
                score = mv_soup.find("div", class_="user_score_chart").get("data-percent")
                title = mv_soup.find("div", class_="title").h2.a.text
                genres_m = mv_soup.find_all("span", class_="genres")
                genres = [gen.a.text for gen in genres_m]
                length = mv_soup.find("span", class_="runtime").text.strip()

                revenue_text = None
                budget_text = None
                facts = mv_soup.find("section", class_="facts left_column").find_all("p")
                for p in facts:
                    if "Revenue" in p.text:
                        revenue_text = p.text.split(' ')[1].replace('$', '')
                    elif "Budget" in p.text:
                        budget_text = p.text.split(' ')[1].replace('$', '')
                
                release = mv_soup.find("span", class_="release").text.strip().split(' ')[0]

                page_movies.append(Movie(title=title, score=score, release=release, genre=genres, revenue=revenue_text, budget=budget_text, duration=convert_to_hours(length)))
            
            except Exception as e:
                print(f"Error processing movie {mv.h2.a['href']} on page {page_num}: {e}")

    except Exception as e:
        print(f"Error processing page {page_num}: {e}")

    finally:
        driver.quit()

    return page_movies


movies = []

try:
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_page = {executor.submit(scrape_page, i): i for i in range(1, pages)}
        for future in concurrent.futures.as_completed(future_to_page):
            page = future_to_page[future]
            try:
                movies.extend(future.result())
            except Exception as e:
                print(f"Page {page} generated an exception: {e}")
except Exception as e:
    print(f"Error with ThreadPoolExecutor: {e}")

try:
    with open('movies.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Genre", "Score", "Release Date", "Budget", "Revenue", "Duration"])
        for movie in movies:
            writer.writerow([movie.title, movie.genre, movie.score, movie.release, movie.budget, movie.revenue, movie.duration])
except Exception as e:
    print(f"Error writing to CSV: {e}")
