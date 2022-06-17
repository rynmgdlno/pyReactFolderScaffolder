import json
import os
from textStrings import reactComponent
with open('structure.json') as structure:
    data = json.load(structure)

def writeComponent(string):
    try:
        with open('index.js', 'w') as component:
            component.write(string)
    finally:
        component.close()

def process(node):
    type = node['type']
    name = node['name']
    if type == 'file':
        try:
            f = open(name, 'w', encoding='utf-8')
        finally: 
            f.close()
    if type == 'directory':
        os.mkdir(name)
        if 'children' in node:
            os.chdir(f"./{name}")
            for i in node['children']:
                process(i)
            os.chdir('../')
    if type == 'component-folder':
        os.mkdir(name)
        os.chdir(f"./{name}")
        try:
            scss = open(f'{name}.scss', 'w')
        finally:
            scss.close()
        writeComponent(reactComponent(name))
        os.chdir('../')  


for i in data:
    process(i)


