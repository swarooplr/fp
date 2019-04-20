import json
from english_brat import final_builder_ui
import os
import random

def buid_brat(text,annotated):


    docData = {}
    docData['text'] = text
    docData['entities'] = []

    start_index = 0
    end_index = 0
    counter = 0
    search_string = text

    for token in annotated:

        entity = []
        entity.append('T'+str(counter))
        entity.append(token[1])

        start_index = end_index + search_string.find(token[0])
        end_index = start_index + len(token[0])

        entity.append([[start_index,end_index]])
        docData['entities'].append(entity)

        counter += 1
        search_string = text[end_index:]

        print(search_string)


    collData = {}
    collData['entity_types'] = []

    tags = set()
    for token in annotated:
        tags.add(token[1])

    colours = open(os.path.join(os.path.dirname(__file__), '../misc/colours.txt')).read().splitlines()


    for tag in tags:
        entity = {}
        entity['type'] = tag
        entity['labels'] = [tag]
        entity['borderColor'] = 'darken'
        entity['bgColor'] = colours[random.randint(0,len(colours)-1)]
        collData['entity_types'].append(entity)

    docData = json.dumps(docData,sort_keys=True,indent=4)
    collData = json.dumps(collData,sort_keys=True,indent=4)



    final_builder_ui.build(docData,collData)


