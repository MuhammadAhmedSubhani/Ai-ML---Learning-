import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import accuracy, pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return "a" # adjective
    elif tag.startswith("V"):
        return "v" # verb
    elif  tag.startswith("N"):
        return "n"   # noun
    elif tag.startswith("R"):
        return "r" # adverb
    else:
        return "n" # noun

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

    pos_tags = pos_tag(filtered_tokens)

    lemmatized_tokens = []

    for token, (_, tag) in zip(filtered_tokens, pos_tags):
        lemmatized_token = lemmatizer.lemmatize(token, get_wordnet_pos(tag))
        lemmatized_tokens.append(lemmatized_token)

    return lemmatized_tokens


def main():

    # Sample texts for demonstration
    texts = [
    "I absolutely LOVED this movie!!!",
    "The actors were running around everywhere.",
    "This product is amazing and useful."
    ]

    # Define the target labels for the texts
    y = [
    "positive",
    "negative",
    "positive"
    ]
    
    # Preprocess the texts
    cleaned_texts = []
    for text in texts:
        cleaned = preprocess_text(text)
        cleaned_text = " ".join(cleaned)
        cleaned_texts.append(cleaned_text)
    
    # Convert the cleaned texts into TF-IDF features
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(cleaned_texts)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Model training
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Model prediction
    predictions = model.predict(X_test)
    print("Predictions:", predictions)
    print("Actual:", y_test)

    #Accuracy check
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)

    #F1 Score and Confusion Matrix
    print(classification_report(y_test, predictions))

main()