from sklearn.feature_extraction.text import TfidfVectorizer

texts = [
    "I love this movie",
    "This movie is terrible",
    "I love the acting"
]

vectorizer = TfidfVectorizer() # Beginner , but use below code always as in ML we will use X as Input and Y as Output
X = vectorizer.fit_transform(texts)

print("Unique Words ",vectorizer.get_feature_names_out()) # To see Unique Words 
print( "In Array ",X.toarray() )

print("Shape ",X.shape) # 3 documents × 7 features
print("Vocabulary ",vectorizer.vocabulary_)