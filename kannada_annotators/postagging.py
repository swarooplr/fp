# -*- coding: utf-8 -*-

import nltk
import pickle
import os
from kannada_brat import postagging_ui
from kannada_annotators import Trie,Word
from sklearn_crfsuite import CRF
from pandas import read_csv



""" Global Data """
t = Trie()
model = CRF()
t = pickle.load(open(os.path.join(os.path.dirname(__file__), '../misc/words_with_root_pos.pickle'),"rb"))
d = dict()
d = pickle.load(open(os.path.join(os.path.dirname(__file__), '../misc/wordtorootdict.pickle'),"rb"))




# Features extraction functions

def root(word):
    try:
        return d[word]
    except:
        return word

def tense(word):
    try:
        x = t.find_tense(word)
        # print x
        return list(x)[0][0]
    except Exception as e:
        pass
        # print e
    return "none"

def previous_word_tense(word,index,pos):
    if index == 0:
        return "none"
    try:
        x = t.find_tense(word) + " " +pos
        return list(x)[0][0]
    except Exception as e:
        pass
    return "none"

def previous_3word(sentence,index):
    temp=[]
    if index - 1 >= 0:
        temp.append(sentence[index - 1])
    else:
        temp.append('')
    if index - 2 >= 0:
        temp.append(sentence[index - 2])
    else:
        temp.append('')

    if index-3>=0:
        temp.append(sentence[index-3])
    else:
        temp.append('')


    return temp


def next_3word(sentence, index):

    temp=[]
    if index + 1 <= len(sentence) - 1:
        temp.append(sentence[index + 1])
    else:
        temp.append('')

    if index + 2 <=len(sentence)-1:
        temp.append(sentence[index + 2])
    else:
        temp.append('')


    if index+3<=len(sentence)-1:
        temp.append(sentence[index+3])
    else:
        temp.append('')


    return temp


def digit(word):
    if word.isdigit():
        return True

    for i in word:
        if ord(i) < 3302 or ord(i) > 3313:
            return False

    return True


def has_aplha_numeric(word):

    for i in word:
        if i<3200 or i>3277:
            return True

    return False

# End of feature extraction function


""" Features used """

def features(sentence, index):

    prev_word = previous_3word(sentence, index)
    next_word = next_3word(sentence, index)

    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        '1st_prev_word':prev_word[0],
        '2nd_prev_word':prev_word[1],
        '3rd_prev_word':prev_word[2],
        '1st_next_word':next_word[0],
        '2nd_next_word':next_word[1],
        '3rd_next_word': next_word[2],
         'is_numeric': digit(sentence[index]),
        'suffix':(sentence[index])[len(sentence[index])-3:],
        'length':len(sentence[index]) > 3,
        'tense':tense(root(sentence[index])),
        'previous_word_tense': previous_word_tense(sentence[index-1],index,sentence[index]),
        'next_word_tense':"none" if index == len(sentence)-1 else tense(sentence[index+1]),
        'root':root(sentence[index]),
        'has_aplha':has_aplha_numeric(sentence[index])
    }

""" End of Features used """


"""POS tagging function calls"""

def untag(tagged_sentence):
    return [w for w, t in tagged_sentence]

def pos_tag(sentence):
    sentence_features = [features(sentence, index) for index in range(len(sentence))]
    # print(sentence_features)
    return list(zip(sentence, model.predict([sentence_features])[0]))


"""END of POS tagging function calls"""







def pos(textval):

        try:
            # load model
            with open(os.path.join(os.path.dirname(__file__), '../misc/pos_model.pickle'), 'rb') as f:
                global model
                model = pickle.load(f)



            tokenized = nltk.word_tokenize(textval,preserve_line=False)
            tagged = pos_tag(tokenized)
            # print(tagged)
        except Exception as e:
            print(str(e))

        postagging_ui.buid_brat(textval, tagged)
        return tagged




# pos("hi there boys. how are you doing")
# pos("ಆ ಜಿಂಕೇನ ಅಟ್ಟಿಸಿಕೊಂಡು ಮನೆಯಿಂದ ಒಡವೆ ದೂರಕ್ಕೆ ಕರ್ಕೊಂಡು ಹೋಗಿ .")
# print pos(u"ರಾಮ್ ಶಾಲೆಗೆ ಹೋಗುತಿದನು. ಪಲ್ಲವಿ ಅವನ ಸಹಪಾಠಿಯಾಗಿದಾಳು. ಅವಳಿಗೆ ಅವನ ಮೇಲೆ ಪ್ರೀತಿ ಹುಟ್ಟಿತು.ರಕ್ಷಿತ್ ಒಬ್ಬ ಗಾಂಡು, ಅವನಿಗೆ ನಾರಾ ಇಲ್ಲ.")

# ಆ ಜಿಂಕೇನ ಅಟ್ಟಿಸಿಕೊಂಡು ಮನೆಯಿಂದ ಒಡವೆ ದೂರಕ್ಕೆ ಕರ್ಕೊಂಡು ಹೋಗಿ .
# data = read_csv('/home/swaroop/NLP/Kannada/datasets/postagged_data_',sep=',',encoding='utf-8')
# count = 0
# for _,i in data.iterrows():
#     count += 1
#     try:
#         t.insert(Word(i["root_word"],i["pos"]))
#         print(i['root_word'])
#     except Exception as e:
#         print e
#
# pickle.dump(t,open("words_with_root_pos.pickle","wb"))