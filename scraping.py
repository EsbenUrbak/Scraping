# import statements
import requests
from bs4 import BeautifulSoup

# fetch web page
r = requests.get("https://www.udacity.com/courses/all")
soup = BeautifulSoup(r.text, "lxml")

# Find all course summaries
summaries = soup.find_all("li", {"class":"catalog-cards__list__item"})
print('Number of Courses:', len(summaries))

# print the first summary in summaries
print(summaries[0].prettify())
# Extract course title
summaries[0].select_one("h2").get_text().strip()

# Extract school
summaries[0].select_one("h3").get_text().strip()


#collecting names and school for ALL course listings
courses = []
for summary in summaries:
    # append name and school of each summary to courses list
    title = summary.select_one("h2").get_text().strip()
    school = summary.select_one("h3").get_text().strip()
    courses.append((title, school))

# display results
print(len(courses), "course summaries found. Sample:")
courses[:20]

#making lower case:
text = text.lower()

# removing punctions etc
import re
text = re.sub(r"[^a-zA-Z0-9]"," ",text)

# import statements
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

text = "Dr. Smith graduated from the University of Washington. He later started an analytics firm called Lux, which catered to enterprise customers."
print(text)

# Split text into words using NLTK
words = word_tokenize(text)
print(words)

# Remove stop words
words = [w for w in words if w not in stopwords.words("english")]
print(words)


from nltk import pos_tag


#Lemmatize
from nltk.stem.wordnet import WordNetLemmatizer

# Reduce words to their root form
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)

# Lemmatize verbs by specifying pos
lemmed = [WordNetLemmatizer().lemmatize(w, pos='v') for w in lemmed]
print(lemmed)
