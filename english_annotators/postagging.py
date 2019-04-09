import nltk
from english_brat import postagging_ui

def pos(textval):

        try:
            tokenized = nltk.word_tokenize(textval,preserve_line=False)
            tagged = nltk.pos_tag(tokenized)

        except Exception as e:
            print(str(e))

        postagging_ui.buid_brat(textval, tagged)
        return tagged


# pos("hi there boys. how are you doing")
