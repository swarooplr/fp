from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
def process_content(textval):

        st = StanfordNERTagger('/home/sourabh/project/stanford-ner-2015-04-20/classifiers/english.all.3class.distsim.crf.ser.gz',
                               '/home/sourabh/project/stanford-ner-2015-04-20/stanford-ner.jar',
                               encoding='utf-8')

        #text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Wall Street Journal.'

        tokenized_text = word_tokenize(textval)
        classified_text = st.tag(tokenized_text)

        return classified_text