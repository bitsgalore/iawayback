from setuptools import setup


setup(
    name='ia_wayback',
    version='0.0.1',
    author='Johan van der Knijff',
    url='https://github.com/jjjake/ia-wayback',
    description=('A simple, minimal Python wrapper around '
                 'Internet Archive\'s Wayback Machine APIs'),
    py_modules=['ia_wayback', 'docopt'],
    install_requires=['internetarchive'],
    entry_points={
        'internetarchive.cli.plugins': [
            'ia_wayback = ia_wayback',
        ],
        'console_scripts': [
            'ia-wayback = ia_wayback:main',
        ],
    },
    tests_require=[
        'pytest',
        'pytest-pep8',
    ],
)
