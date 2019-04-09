from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
def stem(textval):
    new_text = textval
    ps = PorterStemmer()

    words = word_tokenize(new_text)

    tagged=[]
    for w in words:
        tagged.append(ps.stem(w))

    return(tagged)
