from setuptools import setup, find_packages

setup(
    name= 'clint',
    version= '0.4.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires= [],
    entry_points= {
        'console_scripts': [
            'clint = clint.main:main'
        ]
    }
)
