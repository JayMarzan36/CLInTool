# clint
My homemade CLI tool **clint** (CLI-n-tool).

## Arguments
As of version `0.2.1` there are 3 main arguments
*  pg
*  sg
*  mg

If none of the arguments are given the additional arguments, the user will be prompted for them instead.

### pg
pg or project generation, is the keyword for generating projects using user defined templates

#### pg additional args
*  -n, name
*  -l, language
*  --git, initializing git repository
*  --venv, creating a virtual enviornment (note only for python as of now)


### sg
sg or script generation, is the keyword for generating a template script file (.sh or .bat depending on operating system).

#### sg additional args
* -n, name

### mg
mg or make global, makes a script of choice global by adding to either system $PATH or to /usr/local/bin depening on the operating system.

### mg additional args
* -n, name

## Generating Projects
**clint** is able to generate projects based on user defined templates. As of version `0.2.1` these templates are defined using json and need to be formated in the following way.

~~~json
{
  "files" : [
    {
      "numOfFiles" : # Number of files that are part of the project template
    },
    {
      "name" : # Name of the file including the extension,
      "content" : # Content of the file
    }
  ]
}
~~~

In the `numOfFiles` section this is where you put the number of files that are part of the project template, represented as a integar.

After that you have `name` which is the name of the file plus the extension of the file. And part of this section is the `content` section where you put the content of the file.

The sections where you define the file and the content, you can add more than one depending on how many files you want part of the project.

**As of version `0.2.1`, all the files defined in the templates are put in the same directory**

### Example of template
This is an example of the default python template
~~~json
{
    "files": [
        {
            "numOfFiles" : 2
        },
        {
            "name": "main.py",
            "content": "def main() -> None:\n   pass\n\nif __name__ == '__main__':\n    main()"
        },
        {
            "name": "requirements.txt",
            "content": "requirements of project"
        }
    ]
}
~~~

## Generating Scripts
**clint** is able to generate a script based on a user defined template, either .sh or .bat depending on the operating system.

The template is similar to the generating project template but there is no `numOfFiles`.
