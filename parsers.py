import os
from componentGenerators import *


def writeComponent(string):
    try:
        with open('index.js', 'w') as component:
            component.write(string)
    finally:
        component.close()


def process(node, projectType):
    type = node['type']
    name = node['name']
    if type in ['component', 'page']:
        os.mkdir(name)
        os.chdir(f"./{name}")
        writeComponent(
            nextPageComponent(name)
            if type == 'page'
            else reactComponent(name)
        )
        try:
            scss = (
                open(f'{name}.module.scss', 'w')
                if type == 'page'
                else open(f'{name}.scss', 'w')
            )
        finally:
            scss.close()
        os.chdir('../')
    if type == 'directory':
        if (
            projectType == 'nextjs' and
            name not in ['api', 'pages', 'public', 'styles']
        ):
            os.mkdir(name)
        else:
            os.mkdir(name)
        if 'children' in node:
            os.chdir(f"./{name}")
            for child in node['children']:
                process(child, projectType)
            os.chdir('../')
    if type == 'file':
        try:
            f = open(name, 'w', encoding='utf-8')
        finally:
            f.close()
