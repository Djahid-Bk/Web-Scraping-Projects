from bs4 import BeautifulSoup
import requests
import csv

csv_file=open("books.csv","w")
csv_writter=csv.writer(csv_file)
csv_writter.writerow(["Ttile","Price","Availibility"])

main_link="https://books.toscrape.com"
add="https://books.toscrape.com/"
added=""

while(main_link):
    page=requests.get(main_link)
    soup=BeautifulSoup(page.text,"lxml")
    link_list=soup.find_all("h3")
    links=[add+link.a["href"] for link in link_list]
    
    for link in links:
        book=requests.get(link)
        book_soup=BeautifulSoup(book.text,"lxml")
        title=book_soup.find("h1").text
        price=book_soup.find("p",class_="price_color").text.strip()[1::]
        availbilty=book_soup.find("p",class_="instock availability").text.strip()
  
        csv_writter.writerow([title,price,availbilty])

    next=soup.find("li",class_="next")
    next_link=next.a["href"]
    main_link="https://books.toscrape.com/"+added+next_link
    add="https://books.toscrape.com/catalogue/"
    added="catalogue/"

csv_file.close()