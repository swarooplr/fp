#!/usr/bin/env python
# coding: utf-8


from nltk.cluster.util import cosine_distance
import numpy as np
from nltk import  sent_tokenize
import  codecs
import networkx as nx


def sentence_similarity(sent1, sent2):

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        vector1[all_words.index(w)] += 1

    for w in sent2:
        vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2])

    return similarity_matrix


def generate_summary(article, top_n=5):
    summarize_text = []

    #Sentence Tokenization
    sentences = sent_tokenize(article)

    #Building similarity matrix
    sentence_similarity_martix = build_similarity_matrix(sentences)

    #  Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Sort  and pick top sentences
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    #print("Indexes of top ranked_sentence order are ", ranked_sentence)

    sent_len=len(sentences)
    print(sent_len)
    if sent_len < top_n:
        top_n=sent_len

    for i in range(top_n):
        summarize_text.append(ranked_sentence[i][1])


    return ' '.join(summarize_text)



# healthDoc=codecs.open("/home/rakshith/PycharmProjects/NaturalLanguage/sports.txt",encoding="utf-8").read().split('+')
# article=healthDoc[3]
# print(article)
# print(generate_summary(article))
