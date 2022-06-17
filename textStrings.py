# reactComponent = f'react component called {name}'
def reactComponent(name):
  return f"""import React from 'react'\n\nimport './{name}.scss'\n\n"""\
  f"""const {name} = () => {{\n  return (\n    <div>\n\n    </div>\n  )\n}}\n\n"""\
  f"""export default {name}"""

def nextPageComponent(name):
  return f"""stuff here"""

