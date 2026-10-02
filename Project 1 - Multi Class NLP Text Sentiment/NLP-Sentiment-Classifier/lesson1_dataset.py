# x = input data , y = Labels or Targets
# x = tests, y = labels

texts = [
    "I absolutely loved this movie",
    "This movie was terrible",
    "The movie started at 8 PM",
    "I really enjoyed this product",
    "I hate this service",
    "The package arrived today"
]

labels = [
    "Positive",
    "Negative",
    "Neutral",
    "Positive",
    "Negative",
    "Neutral"
]

X = texts
y = labels

print("\nX:")
print(X)

print("\ny:")
print(y)

print("\nClasses:")
print(set(y)) # remove duplicates and get unique classes

# Every sentence is a text and every text has a label. So, the number of texts and labels should be the same.
print("\nNumber of texts:", len(X)) 
print("Number of labels:", len(y))

