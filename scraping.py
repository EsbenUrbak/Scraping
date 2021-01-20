# import statements
import requests
from bs4 import BeautifulSoup

# fetch web page
r = requests.get("https://www.udacity.com/courses/all")
soup = BeautifulSoup(r.text, "lxml")

# Find all course summaries
summaries = soup.find_all("li", {"class":"catalog-cards__list__item"})
print('Number of Courses:', len(summaries))
