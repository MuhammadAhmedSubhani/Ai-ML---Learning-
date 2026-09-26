import nltk
import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

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


def main():

    tags = ["NNS", "VBG", "RB", "JJ"]
    for tag in tags:
        print(tag, get_wordnet_pos(tag))

if __name__ == "__main__":
    main()