# import spacy
# nlp = spacy.load('en_core_web_md')
# # nlp = spacy.load('en')
# tokens = nlp(u'dog cat banana')
# print(tokens)
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
#
# def coreference(textval):
#     import json
#     from stanfordcorenlp import StanfordCoreNLP
#
#     nlp = StanfordCoreNLP(r'/home/swaroop/stanford-corenlp-full-2018-01-31', quiet=False)
#     props = {'annotators': 'coref', 'pipelineLanguage': 'en'}
#
#     text = 'Barack Obama was born in Hawaii.  He is the president. Obama was elected in 2008.'
#     result = json.loads(nlp.annotate(textval, properties=props))
#
#     num, mentions = result['corefs'].items()[0]
#     for mention in mentions:
#         print(mention)