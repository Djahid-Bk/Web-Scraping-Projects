# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import csv

# Create a CSV file for storing book data
csv_file = open("books.csv", "w",encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Title", "Price", "Availability"])

# Initialize the main link and other variables
main_link = "https://books.toscrape.com"
add = "https://books.toscrape.com/"
added = ""
i=0
# Loop through pages to scrape book data
print("scraping...")

while main_link:
    # Fetch the HTML content of the current page
    page = requests.get(main_link)
    soup = BeautifulSoup(page.text, "lxml")

    # Extract links to individual book pages
    link_list = soup.find_all("h3")
    links = [add + link.a["href"] for link in link_list]

    # Process each book page
    for link in links:
        book = requests.get(link)
        book_soup = BeautifulSoup(book.text, "lxml")

        # Extract title, price, and availability
        title = book_soup.find("h1").text
        price = book_soup.find("p", class_="price_color").text.strip()[1:]
        availability = book_soup.find("p", class_="instock availability").text.strip()

        # Write data to the CSV file
        csv_writer.writerow([title, price, availability])

    # Move to the next page (if available)
        
    next_page = soup.find("li", class_="next")
    if next_page and next_page.a:
        next_link = next_page.a["href"]
        main_link = "https://books.toscrape.com/" + added + next_link
    else:
        main_link=None
    
    add = "https://books.toscrape.com/catalogue/"
    added = "catalogue/"
    i=i+1
    print(f"pages scraped: {i}")

# Close the CSV file
csv_file.close()
print("done.")
