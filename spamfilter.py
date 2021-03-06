import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

corpus = ["The first time you see The Second Renaissance it may look boring.",
        "Look at it at least twice and definitely watch part 2.",
        "It will change your view of the matrix.",
        "Are the human people the ones who started the war?",
        "Is AI a bad thing ?"]

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def tokenize(text):
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())

    # tokenize text
    tokens = word_tokenize(text)

    # lemmatize andremove stop words
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    return tokens

# bag of words

from sklearn.feature_extraction.text import CountVectorizer

# initialize count vectorizer object
vect = CountVectorizer(tokenizer=tokenize)

# get counts of each token (word) in text data
X = vect.fit_transform(corpus)

# convert sparse matrix to numpy array to view
X.toarray()

# view token vocabulary and counts
vect.vocabulary_

#TfidfTransformer
from sklearn.feature_extraction.text import TfidfTransformer

# initialize tf-idf transformer object
transformer = TfidfTransformer(smooth_idf=False)

# use counts from count vectorizer results to compute tf-idf values
tfidf = transformer.fit_transform(X)

# convert sparse matrix to numpy array to view
tfidf.toarray()

#TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# initialize tf-idf vectorizer object
vectorizer = TfidfVectorizer()

# compute bag of word counts and tf-idf values
X = vectorizer.fit_transform(corpus)

# convert sparse matrix to numpy array to view
X.toarray()



# tokenize text function:

def tokenize(text):
    # get list of all urls using regex
    # replace each url in text string with placeholder
    #detected_urls = []
    #text_without_url = []
    #for sentence in text:
       # detected_urls_sentence = re.findall(url_regex,sentence)
       # detected_urls.append(detected_urls_sentence)
       # text_without_url_sentence = re.sub(url_regex,"urlplaceholder",sentence)
       # text_without_url.append(text_without_url_sentence)
    detected_urls_sentence = re.findall(url_regex,text)
    text_without_url_sentence = re.sub(url_regex,"urlplaceholder",text)

    #print(text_without_url_sentence)
    # tokenize text
    tokens = word_tokenize(text_without_url_sentence)
    #print(tokens)
    # initiate lemmatizer
    lemmatizer = WordNetLemmatizer()

    # iterate through each token
    clean_tokens = []
    for tok in tokens:
        #print(tok)
        # lemmatize, normalize case, and remove leading/trailing white space
        clean_tok = re.sub(r"[^a-zA-Z0-9]", " ", lemmatizer.lemmatize(tok).lower())
        clean_tokens.append(clean_tok)
    return clean_tokens
