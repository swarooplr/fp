import os
import pickle
import nltk
import numpy as np
import pandas as pd
from kannada_brat import postagging_ui



def name_count(name):
    arr = np.zeros(30)
    arr[0] = ord(name[-2])-3200
    arr[1] = ord(name[-1])-3200
    arr[3] = ord(name[-1])-3200

    return arr


def classify_gender(textval):
    with open(os.path.join(os.path.dirname(__file__), '../misc/gender_classification.pickle'), 'rb') as f:
        global model
        model = pickle.load(f)

    tokens = nltk.word_tokenize(textval, preserve_line=False)
    tagged = []
    for i in tokens:
        try:
            name_map = np.vectorize(name_count, otypes=[np.ndarray])
            df = pd.DataFrame([(i, 1)], columns=["name", "gender"])
            Xlist = name_map(df["name"])

            y = Xlist.tolist()
            gno = model.predict(y)[0]
            if gno == 1:
                gender = "Male"
            else:
                gender = "Female"
            tagged.append((i, gender))
        except Exception as e:
            pass

    postagging_ui.buid_brat(textval, tagged)
    return tagged


