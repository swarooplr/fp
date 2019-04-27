import nltk
from english_brat import postagging_ui

def ner(textval):

    tagged = []

    for sent in nltk.sent_tokenize(textval):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                tagged.append((' '.join(c[0] for c in chunk),chunk.label()))
                print(chunk.label(), ' '.join(c[0] for c in chunk))

    postagging_ui.buid_brat(textval, tagged)
    return tagged

# process_content("hi")

