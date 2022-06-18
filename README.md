# pyReactFolderScaffolder
A Python script for scaffolding basic React or Next.js folder structure from a JSON (YAML is in the works) tree representing the project. (Currently only for Unix based OSes)

### Basic Usage:
To use simply clone this repo into your projects root directory, write your project's hierarchy JSON file in the root directory (ideally written while planning out the project),
and title it "structure.json",
then call the script in your terminal as such: "python3 ./projectScaffolder/main.py".

You can also run it without providing "structure.json" and it will use the example in "example.json".

### JSON Formatting:
The JSON file must contain only a single array with two entries, the first of which is an object with a single {key: value} pair to denote the project type, the second is an array of nodes. Each node must be an object with the required properties "name" and "type", who's values must be strings correlating to the currently accepted node types, with an optional property "children" who's value must be an array of nodes. Simply omit the "children" property if there are no children. Directories, Components, and Pages can have children.

Example:
[
  {
    "projectType": "react"
  },
  [
    {
      "name": "src",
      "type": "directory",
      "children": [
        {
          "name": "customButton",
          "type": "component"
        },
        {
          "name": "helperFunctions.js",
          "type": "file"
        }
      ]
    },
    "name": "pages",
    "type": "directory",
    "children": [
      {
        "name": "aboutMe",
        "type": "page",
      },
    ]
  ]
]

### Project Types:
The script currently recognizes two "projectTypes": "react" and "nextjs". 

Using "nextjs" simply prevents the script from trying to recreate folders that Next provides, namely "pages", "pages/api", "public", and "styles", and also offers the node type "page".

### Node Types:
- "component": This creates a folder with the given name, then populates it with a {name}.scss file and an index.js, which will contain a functional component boilerplate with proper naming and stylesheet import already applied.
- "directory": Self explanatory. Use the optional "children" property to populate the directory.
- "file": Simply creates an empty file with the given name.
- "page": This uses the same logic as the "component" type, though uses scss modules, imports next/head, and adds the head to the component. Should only be used with "projectType": "nextjs", though can be used otherwise if for some reason you want to. 

### Modification and Custom Node Types:
The component generators (componentGenerators.py) just take the name and return format strings with appropriate naming.
writeComponent() is a simple helper function which creates an index.js and writes to it whatever string is passed.

If you create any custom components or parsers feel free to open a pull request and I'll add them :)

