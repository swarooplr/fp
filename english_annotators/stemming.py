from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from english_brat import postagging_ui

def stem(textval):
    new_text = textval
    ps = PorterStemmer()

    words = word_tokenize(new_text)

    tagged=[]
    for w in words:
        tagged.append((w,ps.stem(w)))
    postagging_ui.buid_brat(textval, tagged)
    return tagged
