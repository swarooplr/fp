# -*- coding: utf-8 -*-

import pickle
import codecs
import string
from pandas import read_csv
from kannada_annotators import Trie,Word
# from stemming import basic_split,plurals_split
import os
from sandhi_splitting import lopa, aagama, aadesha, savarnadeerga, guna, vurdhi, yann
import nltk
from english_brat import postagging_ui








t = Trie()
t = pickle.load(open(os.path.join(os.path.dirname(__file__), '../misc/triecompoundwordsincluded.pickle'),"rb"))
rootwords = pickle.load(open(os.path.join(os.path.dirname(__file__), '../misc/trierootwords.pickle'),"rb"))

def display_split(word ,splits):

    print word,"split into:  ",
    try:
        for split in splits:
            print split,
    except Exception as e:
        print e
    print

def single_split(word,root):
    splits = []

    if True:
    #if not root.is_present(word):
        for func in (lopa,aagama, aadesha, savarnadeerga, guna, vurdhi, yann):
            splits = func(root, word)
            if len(splits) != 0:
                return splits[0]

    return splits

def mulitiple_split(word,root,combined):

    splits = []
    if len(word) <= 2:
        return splits

    # splits = single_split(word,root)
    # if len(splits) > 0:return splits


    for func in (lopa,aagama,aadesha,savarnadeerga,guna,vurdhi,yann):
            splits = func(combined,word)
            if len(splits) != 0:
                    splits = splits[0]
                    first = mulitiple_split(splits[0],root,combined)
                    second = mulitiple_split(splits[1],root,combined)

                    new_splits = []
                    if len(first) != 0:
                        for split in first:
                            new_splits.append(split)
                    else:
                        new_splits.append(splits[0])

                    if len(second) != 0:
                        for split in second:
                            new_splits.append(split)
                    else:
                        new_splits.append(splits[1])

                    return  new_splits


    return splits


def split_mulitple_handler(word):
    x = mulitiple_split(word,rootwords,t)
    if len(x) == 0:
        return word

    new_text = ""
    for i in x:
        new_text += i + " "
    return new_text

def sandhi_split(textval):
    tokens = nltk.word_tokenize(textval,preserve_line=False)
    print(len(tokens))
    print tokens
    tagged = []
    for i in tokens:
        try:
            split = split_mulitple_handler(i)
            if split != i:
                tagged.append((i, split_mulitple_handler(i)))
        except Exception as e:
            pass

    for i in tagged:
        print i[0],i[1]
    postagging_ui.buid_brat(textval, tagged)
    return tagged

# sandhi_split(u'ಜಿಂಕೇನ ಅಟ್ಟಿಸಿಕೊಂಡು ಮನೆಯಿಂದ ಒಡವೆ ದೂರಕ್ಕೆ ಕರ್ಕೊಂಡು ಹೋಗಿ .')


# for i in test_words:
#     print split_mulitple_handler(i)


# count  = 0
# for i in test_words:
#     x = mulitiple_split(i,rootwords,t)
#
#     if len(x) > 0:
#         display_split(i,mulitiple_split(i,rootwords,t))
#
#     if len(x)>2:
#         count +=1
# print count

    # if len(basic_split(i,rootwords)) != 0:
    #     basic_set.append(basic_split(i,rootwords))
    #
    # if len(plurals_split(i,rootwords)) !=0:
    #     plural_set.append(plurals_split(i,rootwords))
    #     unclean_words.add(i)



""" to add root words"""
# t = Trie()
# pronoun_list = codecs.open("/home/swaroop/NLP/Kannada/datasets/baseKannadaWords","r",encoding='utf-8').read().splitlines()
# pronoun_list = [x.strip(string.whitespace) for x in pronoun_list]
# for i in pronoun_list:
#     t.insert(Word(i,None))
#
#
# pickle.dump(t,open("trierootwords.pickle","w"))
# pickle.dump(t,open("trierootwords.pickle","w"))
# t = pickle.load(open("triecompoundwordsincluded.pickle","rb"))
# rootwords = pickle.load(open("trierootwords.pickle","rb"))
# data = read_csv('/home/swaroop/NLP/Kannada/datasets/postagged_data_',sep=',',encoding='utf-8')
#
# for _,i in data.iterrows():
#     try:
#         t.insert(Word(i["word"],i["pos"]))
#     except Exception as e:
#         pass
#         # print e
# pickle.dump(t,open("trierootwords.pickle","wb"))
# #
# print("loading data for sandhi splitting completed...")
# quit()


"""
    code to show sandhi split examples
"""
# test_words = [u'ಜಾತ್ಯಾತೀತ',u'ಕರೆದರು',u'ಗಾಬರಿಯಾದ',u'ಏಳೆಂಟು',u'ಸಾರಿದ',u'ಇರುವೆಗಳು',u'ನನ್ನಿಂದ',u'ಖಚಿತವಾಗಿದೆ',u'ಕೊಡುವುದು']

#text = codecs.open("/home/swaroop/NLP/Kannada/datasets/article1",encoding="utf-8").read()
#test_words = text.split(" ")
#test_words = set(test_words)
# valid = []
# split_words = set()

# for word in test_words:
#     flag = False
#     if not rootwords.is_present(word):
#         for func in (lopa,aagama,aadesha,savarnadeerga,guna,vurdhi,yann):
#             splits = func(t,word)
#             if not len(splits) == 0:
#                 print func
#                 for split in splits:
#                     print split[0],split[1]
#                 valid.append(word)
#                 flag = True
#         if flag:
#             print word

# for i in valid:
#     print i


#print len(set(valid))


# t = Trie()
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
# # pickle.dump(t,open("words_with_root_pos.pickle","wb"))
#
# t = Trie()
# a = codecs.open("/home/swaroop/NLP/Kannada/datasets/health.txt","r",encoding='utf-8').read()
# b = codecs.open("/home/swaroop/NLP/Kannada/datasets/politics.txt","r",encoding='utf-8').read()
# c = codecs.open("/home/swaroop/NLP/Kannada/datasets/sports.txt","r",encoding='utf-8').read()
# d = codecs.open("/home/swaroop/NLP/Kannada/datasets/lekhana.txt","r",encoding='utf-8').read()
# e = codecs.open("/home/swaroop/NLP/Kannada/datasets/stories.txt","r",encoding='utf-8').read()
# f = codecs.open("/home/swaroop/NLP/Kannada/datasets/film.txt","r",encoding='utf-8').read()
#
# a += "\n"+b + "\n" + c + "\n" + d + "\n" + e + "\n" + f
#
# def clean(word):
#
#     if len(word) <= 2:
#         return False
#
#     for i in word:
#         if 3200 > ord(i) < 3299:
#             return False
#
#     return True
#
# count = set()
#
# import nltk
#
# l = nltk.word_tokenize(a,preserve_line=False)
# print(len(l))
# for i in l:
#     print(i)
#     if clean(i):
#         #print i
#         count.add(i)
#         t.insert(Word(i, "None"))
#
# print len(count)
#
#
#
# pronoun_list = codecs.open("/home/swaroop/NLP/Kannada/datasets/kannada1.txt","r",encoding='utf-8').read().splitlines()
# pronoun_list = [x.strip(string.whitespace) for x in pronoun_list]
# for i in pronoun_list:
#     count.add(i)
#     t.insert(Word(i, "None"))
#
# # file_handler = codecs.open("/home/swaroop/NLP/Kannada/compoundKannadaWords.txt",'w',encoding="utf-8")
# # for w in count:
# #     file_handler.write(w)
# #     file_handler.write('\n')
#
#
# print (len(count))
#
# pickle.dump(t,open("triecompoundwordsincluded.pickle",'w'))
# quit()






