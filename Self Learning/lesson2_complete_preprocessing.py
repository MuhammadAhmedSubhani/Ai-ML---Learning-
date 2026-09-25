import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):

    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    tokens = word_tokenize(text)

    filtered_tokens = []

    for token in tokens:
        if token not in stop_words:
            filtered_tokens.append(token)

    lemmatized_tokens = []

    for token in filtered_tokens:
        lemmatized_token = lemmatizer.lemmatize(token)
        lemmatized_tokens.append(lemmatized_token)

    return lemmatized_tokens


def main():

    texts = [
    "I absolutely LOVED this movie!!!",
    "The actors were running around everywhere.",
    "This product is amazing and useful."
    ]

    for _ in texts:
        print(preprocess_text(_))
        result = preprocess_text(_)



main()