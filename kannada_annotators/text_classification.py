import pickle
import os
from kannada_brat import summarization_ui


def classify(text):

    category_to_id = {"Health":0,
                      "Politics":1,
                      "Sports":2,
                      "Film":3,
                      "Technical":4
                      }


    with open(os.path.join(os.path.dirname(__file__), '../misc/textclassification.pickle'), 'rb') as f:
        global model
        model = pickle.load(f)

    with open(os.path.join(os.path.dirname(__file__), '../misc/tfidf.pickle'), 'rb') as f:
        global model
        tfidf = pickle.load(f)

    test = tfidf.transform([text])
    index = model.predict(test)[0]
    class_type = ""
    for i in category_to_id.keys():
        if category_to_id[i] == index:
            class_type = i
            break

    summarization_ui.buid_brat(class_type)
    return class_type




