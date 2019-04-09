import os
import codecs

def build(docData,collData):
    prefix1 = 'var collData = '
    prefix2 = 'var docData = '
    suffix = ';\n'

    javascript_code = prefix1 + collData + suffix + prefix2 + docData + suffix

    dirname = os.path.dirname(__file__)
    print(dirname)
    filename = os.path.join(dirname, '../static/bratdata.js')
    print(filename)
    javascript_file = codecs.open(filename, encoding='utf-8', mode='w')
    javascript_file.write(javascript_code)
    javascript_file.close()