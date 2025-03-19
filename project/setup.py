from setuptools import setup, find_packages

def getVersion() -> str:
    return "0.5.0"

setup(
    name= 'clint',
    version= getVersion(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires= [],
    entry_points= {
        'console_scripts': [
            'clint = clint.main:main'
        ]
    }
)
