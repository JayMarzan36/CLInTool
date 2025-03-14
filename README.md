# clint
My homemade CLI tool **clint** (CLI-n-tool).

Most up-to-date version is `0.3.0`

## Arguments
As of version `0.3.0` there are 4 main arguments
*  mp
*  ms
*  mg
*  mt

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
mt or make template, allows the user to make a template either for projects or scripts. This all happens in the command line for now (as of version `0.3.0`). 

**For future feature, im planning on adding a argument that allows the user to "upload" their own template so they don't have to use the command line.**

#### mt additional args
* -n, name
* -c, content
* -t or --type, template type 

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


### Example from projects template
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

The template is similar to the generating project template but there is no `numOfFiles` and no `name` attribute.

There is just a `content` section as the file name is the `name`.

### Example of script template

~~~json
{
    "content" : "Content of the template here"
}
~~~