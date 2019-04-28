# -*- coding: utf-8 -*-

import sys,os,codecs
from kannada_annotators import postagging
from kannada_annotators import gender_classification
from kannada_annotators import sandhi_splitting_main
from kannada_brat import coreference_ui

def coreference(textval):
    pos_tag = postagging.pos(textval)
    proper_noun_list = []
    pronoun_list = []
    boys_name_file = codecs.open(os.path.join(os.path.dirname(__file__), '../misc/boysnamesKN'),encoding='utf-8').readlines()
    girls_name_file = codecs.open(os.path.join(os.path.dirname(__file__), '../misc/girlsnamesKN'),encoding='utf-8').readlines()
    boys_name=[]
    girls_name=[]
    for boys in boys_name_file:
        boys_name.append(boys)
    for  girls in girls_name_file:
        girls_name.append(girls)
    map(unicode,boys_name)
    map(unicode,girls_name)

    for token in pos_tag:

        print token[0] + "hi"
        print token[1]

        if token[1] in ['N__NNP']:
            proper_noun_list.append(token[0])

        if token[1] in ['N__NN'] and (token[0] in boys_name or token[0] in girls_name):
            proper_noun_list.append(token[0])


        if token[1] in ["PR__PRC","PR__PRF","PR__PRI","PR__PRP","PP__PRQ"]:
            pronoun_list.append(token[0])

    male_pronoun_list = {u'ಅವನಿಂದ',u'ಅವನಿಂದಾಗಿ',u'ಅವನು',u'ಅವನಿಗೆ',u'ಅವನ',u'ಅವನನ್ನು',u'ಅವನಿಗೋಸ್ಕರ',u'ಅವನಲ್ಲಿ'}
    female_pronoun_list = {u'ಅವಳು',u'ಅವಳಿಗೆ',u'ಅವಳು',u'ಅವಳಿಂದ',u'ಅವಳಿಗೋಸ್ಕರ',u'ಅವಳನ್ನು',u'ಅವಳಲ್ಲಿ'}

    #classify as male or female
    gender_tagged_propernoun = gender_classification.classify_gender(' '.join(proper_noun_list))
    print(gender_tagged_propernoun)

    gender_tagged_pronoun = []
    for pronoun in pronoun_list:
        if pronoun in male_pronoun_list:
            gender_tagged_pronoun.append((pronoun,"Male"))
        elif pronoun in female_pronoun_list:
            gender_tagged_pronoun.append((pronoun,"Female"))
        else:
            ssplit = sandhi_splitting_main.split_mulitple_handler(pronoun)
            ssplit = ssplit.split(" ")
            if len(set(ssplit).intersection(set(male_pronoun_list))) > 0:
                gender_tagged_pronoun.append((pronoun,"Male"))
            elif len(set(ssplit).intersection(set(female_pronoun_list))) > 0:
                gender_tagged_pronoun.append((pronoun, "Female"))
            else:
                gender_tagged_pronoun.append((pronoun, "Others"))




    coreference_cordinates = []
    search_string = textval
    start = 0
    for pronoun in gender_tagged_pronoun:
        shortest = sys.maxsize
        p1 = search_string.find(pronoun[0], start)
        p3 = -1
        copropernoun = ""
        for propernoun in gender_tagged_propernoun:
            if pronoun[1] == propernoun[1]:
                p2 = search_string.find(propernoun[0])
                if p1 - p2 > 0 and (p1 - p2) < shortest:
                    p3 = p2
                    copropernoun = propernoun[0]
        if p3 != -1:
            coreference_cordinates.append((p3,p3+len(copropernoun),p1,p1+len(pronoun[0])))
        start = p1 + len(pronoun[0])



    # finding duplicates
    search_string = textval
    start = 0
    for propernoun in gender_tagged_propernoun:
        p1 = search_string.find(propernoun[0],start)
        p2 = search_string.find(propernoun[0],start+len(propernoun[0]))
        if p2 != -1:
            coreference_cordinates.append((p1, p1 + len(propernoun[0]), p2, p2 + len(propernoun[0])))
        start = p1 + len(propernoun[0])

    print coreference_cordinates
    for i in coreference_cordinates:
        print(textval[i[0]:i[1]])
        print(textval[i[2]:i[3]])
    coreference_ui.buid_brat(textval,coreference_cordinates)
    return "rakki"



# coreference(u'ರಾಮ್ ಶಾಲೆಗೆ ಹೋಗುತಿದನು. ಪಲ್ಲವಿ ಅವನ ಸಹಪಾಠಿಯಾಗಿದಾಳು. ಅವಳಿಗೆ ಅವನ ಮೇಲೆ ಪ್ರೀತಿ ಹುಟ್ಟಿತು. ')