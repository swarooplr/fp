from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize

def lem(textval):
    new_text =textval
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(new_text)

    tagged = []
    for w in words:
        tagged.append(lemmatizer.lemmatize(w))
    return tagged




