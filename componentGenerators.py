import re

# Formatting Functions:

# Capitalize the component while maintaining camel case:
# ex: someCustomComponent => SomeCustomComponent
def componentName(name):
    return name[0].upper() + name[1:]


# Formats the name with spaces to be readable,
# for instance a <title> meta tag:
# someCustomComponent => Some Custom Component
def formatName(name):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", name)


# Component Generators:
# React functional boilerplate component with named scss import
def reactComponent(name):
    component = componentName(name)
    return (
        f"""import React from 'react'\n\nimport './{name}.scss'\n\n"""
        f"""const {component} = () => {{\n"""
        f"""  return (\n    <div>\n\n    </div>\n  );\n}};\n\n"""
        f"""export default {component}"""
    )


# Next.js page component boilerplate, with named scss module import,
# and next/head import
def nextPageComponent(name):
    component = componentName(name)
    formatted = formatName(component)
    return (
        f"""import Head from "next/head";\n\n"""
        f"""import styles from "./{name}.module.scss";\n\n"""
        f"""const {component} = () => {{\n"""
        f"""  return (\n    <main>\n"""
        f"""      <Head>\n"""
        f"""        <title>{formatted}</title>\n"""
        f"""        <meta name="{formatted}" content="" />\n"""
        f"""        <link rel="icon" href="/favicon.ico" />\n"""
        f"""      </Head>\n"""
        f"""      <div>\n\n"""
        f"""      </div>\n"""
        f"""    </main>\n  );\n}};\n\n"""
        f"""export default {component}"""
    )
