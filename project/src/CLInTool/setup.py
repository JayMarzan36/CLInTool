from setuptools import setup

setup(
    nam= 'CLInTool',
    version= '0.1',
    py_modules= ['CLInTool'],
    install_requires= [],
    entry_points= {
        'console_scripts': [
            'CLInTool = CLInTool.__main__:main'
        ]
    }
)