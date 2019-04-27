import json
from english_brat import final_builder_ui
import os
import random

def buid_brat(text):


    docData = {}
    docData['text'] = text
    docData['entities'] = []

    collData = {}
    collData['entity_types'] = []



    docData = json.dumps(docData,sort_keys=True,indent=4)
    collData = json.dumps(collData,sort_keys=True,indent=4)



    final_builder_ui.build(docData,collData)


