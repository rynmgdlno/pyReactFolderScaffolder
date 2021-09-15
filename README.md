# pyReactFolderScaffolder
Python script for scaffolding a basic React src folder structure and minimum required files based on a JSON outline of the project. Check "structure.json" for a working example.

### Usage:
Each JSON node requires a "name" and "type" attribute. The optional "children" attribute will be recursively processed. 

The script currently recognizes three types:
- "directory"
- "file"
- "component-folder"

'directory' and 'file' will create a directory or file with the given name.
'component-folder' will create a folder with the given name, and populate the folder with an index.js and a 'name'.scss file. 

