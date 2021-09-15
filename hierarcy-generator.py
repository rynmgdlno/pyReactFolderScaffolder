import json
import os
with open('structure.json') as structure:
    data = json.load(structure)

def process(node):
    node_type = node['type']
    name = node['name']
    if node_type == 'file':
        with open(name, 'w') as fp:
            pass
    if node_type == 'directory':
        os.mkdir(name)
        if 'children' in node:
            os.chdir(f"./{name}")
            for i in node['children']:
                process(i)
            os.chdir('../')
    if node_type == 'component-folder':
        os.mkdir(name)
        os.chdir(f"./{name}")
        with open(f'{name}.scss', 'w') as fp:
            pass
        with open('index.js', 'w') as fp:
            pass
        os.chdir('../')  


for i in data:
    process(i)
