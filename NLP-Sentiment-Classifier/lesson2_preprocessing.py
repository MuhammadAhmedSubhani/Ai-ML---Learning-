import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")
nltk.download("wordnet")

text = "I absolutely loved this movie!"
text = text.lower()  
text = text.translate(str.maketrans("", "", string.punctuation)) #removes punctuatuon
stop_words = set(stopwords.words("english")) # removes stop words
lemmatizer = WordNetLemmatizer() # removes inflectional and derivational morphology

tokens = word_tokenize(text)

filtered_tokens = []
for token in tokens:
    if token not in stop_words:
        filtered_tokens.append(token)

lemmatized_tokens = []
for token in filtered_tokens:
    lemmatized_token = lemmatizer.lemmatize(token)
    lemmatized_tokens.append(lemmatized_token)
print(filtered_tokens)