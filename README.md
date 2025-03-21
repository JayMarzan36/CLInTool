# clint
My homemade CLI tool **clint**.

Most up-to-date version is `0.5.2`

## Arguments
As of version `0.5.1` there are 4 main arguments
*  mp
*  ms
*  mg
*  mt
*  at
*  v

If none of the arguments are given the additional arguments, the user will be prompted for them instead.

### mp
mp or make project, is the keyword for generating projects using user defined templates

#### mp additional args
*  -n, name
*  -l, language
*  --git, initializing git repository
*  --venv, creating a virtual enviornment (note only for python as of now)


### ms
ms or make script, is the keyword for generating a template script file (.sh or .bat depending on operating system).

#### ms additional args
* -n, name

### mg
mg or make global, makes a script of choice global by adding to either system $PATH or to /usr/local/bin depening on the operating system.

### mg additional args
* -n, name
  
### mt
mt or make template, allows the user to make a template either for projects or scripts.

#### mt additional args
* -n, name
* -c, content
* -t or --type, template type

### at
at or add template, allows the user to add a template without having to use the command line.

#### at additional args
* -n, name
* -p, path
* -t, --type, template type

### v
v prints out the current version of clint

## Generating Projects
**clint** is able to generate projects based on user defined templates. As of version `0.5.1` these templates are defined using json and need to be formated in the following way.

~~~json
{
  "file" : 
    {
      "name" : # Name of the file including the extension
    },
    {
      "content" : # Content of the file or path to local file
    }
}
~~~

After that you have `fileName` which is the name of the file plus the extension of the file. And part of this section is the `content` section where you put the content of the file.

As of version `0.5.1` you can now specify directories.

Example
~~~json
{
    "dir": [
        {
            "dirName": "src"
        },
        {
            "dirContents": {
                "file": [
                    {
                        "fileName": "main.py"
                    },
                    {
                        "content": "testContent.py"
                    }
                ]
            }
        }
    ],
    "file": [
        {
            "fileName": "setup.py"
        },
        {
            "content": "#HI"
        }
    ]
}
~~~

For making directories in the templates, you specify the name of the directoy with `dirName` and the contents with `dirContents`. In `dirContents` you can specify more directories or files.


## Generating Scripts
**clint** is able to generate a script based on a user defined template, either .sh or .bat depending on the operating system.

The template is similar to the generating project template but there is no `numOfFiles` and no `name` attribute.

There is just a `content` section as the file name is the `name`.

### Example of script template

~~~json
{
    "content" : "Content of the template here"
}
~~~

# To-do
Change template strucutre to be able to specify and make directories
