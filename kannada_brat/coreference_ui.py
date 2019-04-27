import json
from english_brat import final_builder_ui
import os
import random

def buid_brat(text,annotated):


    docData = {}
    docData['text'] = text
    docData['entities'] = []
    docData['relations'] = []

    start_index = 0
    end_index = 0
    counter = 0
    search_string = text

    id_map = {}
    finished_map = {}
    counter = 0
    for token in annotated:
        if not id_map.has_key(token[0]):
            id_map[token[0]] = counter
            counter += 1
            finished_map[token[0]] = True
        if not id_map.has_key(token[2]):
            id_map[token[2]] = counter
            counter += 1
            finished_map[token[2]] = True


    for token in annotated:


        entity = []
        entity.append('T' + str(id_map[token[0]]))
        entity.append('Entity')
        entity.append([[token[0],token[1]]])
        docData['entities'].append(entity)

        counter += 1

        entity = []
        entity.append('T' + str(id_map[token[2]]))
        entity.append('Anaphor')
        entity.append([[token[2], token[3]]])
        docData['entities'].append(entity)

        counter += 1

        docData['relations'].append(
            ['R'+str(counter-1), 'Co-Reference', [['Anaphor', 'T' + str(id_map[token[2]])], ['Entity','T' + str(id_map[token[0]])]]]
        )


    collData = {}
    collData['entity_types'] = []

    tags = set()
    tags.add("Anaphor")
    tags.add("Entity")

    colours = open(os.path.join(os.path.dirname(__file__), '../misc/colours.txt')).read().splitlines()

    collData['relation_types'] = [{
                                      "type": 'Co-Reference',
                                      "labels": ['Co-Reference'],
                                      "dashArray": '3,3',
                                       "color": 'purple',
                                      "args": [
                                      {"role": 'Anaphor', "targets": ['Anaphor']},
                                      {"role": 'Entity', "targets": ['Entity']}
                                      ]
                                }]


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


