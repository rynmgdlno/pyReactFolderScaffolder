import json
from parsers import *


with open('structure.json') as structure:
    data = json.load(structure)

def parse(structure):
    projectType = structure[0]["projectType"]

    if projectType not in ['react', 'nextjs']:
      raise Exception('projectType is not currently supported')

    for i in structure[1]:
        process(i, projectType)


parse(data)
