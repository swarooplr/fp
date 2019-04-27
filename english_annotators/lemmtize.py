from nltk.stem import WordNetLemmatizer
from english_brat import postagging_ui
import nltk

def lem(textval):
    tokens = nltk.word_tokenize(textval, preserve_line=False)

    tagged = []
    for i in tokens:
        try:
            w = WordNetLemmatizer().lemmatize(i)
            tagged.append((i, w))
        except Exception as e:
            print(e)
            pass

    postagging_ui.buid_brat(textval, tagged)
    return tagged


# lem("Going gets tough we break down.")



